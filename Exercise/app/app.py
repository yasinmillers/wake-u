import json
import csv
import io
import traceback
from datetime import datetime

from flask import Flask, request, jsonify, send_file, render_template_string
import yt_dlp

app = Flask(__name__)

# ── Helpers ──────────────────────────────────────────────────────────────────

def _ydl_opts():
    return {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "extract_flat": False,
    }


def _extract(url: str) -> dict:
    with yt_dlp.YoutubeDL(_ydl_opts()) as ydl:
        info = ydl.extract_info(url, download=False)
    return _pick(info)


def _pick(info: dict) -> dict:
    duration = info.get("duration") or 0
    upload = info.get("upload_date") or ""
    if upload:
        upload = f"{upload[:4]}-{upload[4:6]}-{upload[6:8]}"
    return {
        "id": info.get("id", ""),
        "title": info.get("title", ""),
        "url": f"https://www.youtube.com/watch?v={info.get('id', '')}",
        "channel": info.get("uploader") or info.get("channel") or "",
        "channel_url": info.get("uploader_url") or info.get("channel_url") or "",
        "views": info.get("view_count"),
        "likes": info.get("like_count"),
        "comments": info.get("comment_count"),
        "duration": duration,
        "duration_str": f"{duration // 3600}:{(duration % 3600) // 60:02d}:{duration % 60:02d}" if duration else "",
        "upload_date": upload,
        "description": (info.get("description") or "")[:500],
        "thumbnail": info.get("thumbnail") or "",
        "tags": info.get("tags") or [],
        "categories": info.get("categories") or [],
    }


def _search(query: str, n: int = 10):
    opts = {**_ydl_opts(), "extract_flat": "in_playlist"}
    with yt_dlp.YoutubeDL(opts) as ydl:
        result = ydl.extract_info(f"ytsearch{n}:{query}", download=False)
    entries = result.get("entries") or []
    out = []
    for e in entries:
        out.append({
            "id": e.get("id", ""),
            "title": e.get("title", ""),
            "url": e.get("url") or f"https://www.youtube.com/watch?v={e.get('id', '')}",
            "channel": e.get("uploader") or e.get("channel") or "",
            "duration": e.get("duration"),
            "views": e.get("view_count"),
            "thumbnail": e.get("thumbnails", [{}])[-1].get("url", "") if e.get("thumbnails") else "",
        })
    return out


def _channel_videos(url: str, n: int = 30):
    opts = {**_ydl_opts(), "extract_flat": True, "playlistend": n}
    with yt_dlp.YoutubeDL(opts) as ydl:
        result = ydl.extract_info(url, download=False)
    entries = result.get("entries") or []
    out = []
    for e in entries:
        out.append({
            "id": e.get("id", ""),
            "title": e.get("title", ""),
            "url": e.get("url") or f"https://www.youtube.com/watch?v={e.get('id', '')}",
            "channel": e.get("uploader") or e.get("channel") or result.get("uploader") or "",
            "duration": e.get("duration"),
            "views": e.get("view_count"),
        })
    return out


# ── API Routes ───────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/api/video", methods=["POST"])
def api_video():
    url = (request.json or {}).get("url", "").strip()
    if not url:
        return jsonify({"error": "URL is required"}), 400
    try:
        return jsonify(_extract(url))
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/search", methods=["POST"])
def api_search():
    body = request.json or {}
    query = body.get("query", "").strip()
    n = min(int(body.get("count", 10)), 50)
    if not query:
        return jsonify({"error": "Query is required"}), 400
    try:
        return jsonify(_search(query, n))
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/channel", methods=["POST"])
def api_channel():
    body = request.json or {}
    url = body.get("url", "").strip()
    n = min(int(body.get("count", 30)), 100)
    if not url:
        return jsonify({"error": "URL is required"}), 400
    try:
        return jsonify(_channel_videos(url, n))
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/api/export", methods=["POST"])
def api_export():
    body = request.json or {}
    data = body.get("data", [])
    fmt = body.get("format", "json")
    if not data:
        return jsonify({"error": "No data to export"}), 400
    if fmt == "csv":
        si = io.StringIO()
        if data:
            w = csv.DictWriter(si, fieldnames=data[0].keys())
            w.writeheader()
            for row in data:
                clean = {}
                for k, v in row.items():
                    if isinstance(v, list):
                        v = "; ".join(str(i) for i in v)
                    clean[k] = v
                w.writerow(clean)
        buf = io.BytesIO(si.getvalue().encode("utf-8"))
        return send_file(buf, mimetype="text/csv", as_attachment=True, download_name="youtube_data.csv")
    else:
        buf = io.BytesIO(json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8"))
        return send_file(buf, mimetype="application/json", as_attachment=True, download_name="youtube_data.json")


# ── Frontend ─────────────────────────────────────────────────────────────────

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>YouTube Data Collector</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0f0f13;--surface:#1a1a24;--surface2:#24243a;--border:#2e2e48;
  --text:#e4e4f0;--muted:#8888a8;--accent:#7c5cff;--accent2:#5c9cff;
  --red:#ff5c6c;--green:#5cffb0;--radius:12px;
}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);min-height:100vh}
a{color:var(--accent2);text-decoration:none}
a:hover{text-decoration:underline}

/* Layout */
.app{max-width:1100px;margin:0 auto;padding:24px 20px}
header{text-align:center;margin-bottom:32px}
header h1{font-size:1.8rem;font-weight:700;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
header p{color:var(--muted);margin-top:6px;font-size:.95rem}

/* Tabs */
.tabs{display:flex;gap:4px;background:var(--surface);border-radius:var(--radius);padding:4px;margin-bottom:24px}
.tab{flex:1;padding:10px;text-align:center;border-radius:8px;cursor:pointer;font-weight:500;font-size:.9rem;color:var(--muted);transition:.2s}
.tab:hover{color:var(--text)}
.tab.active{background:var(--accent);color:#fff}

/* Panels */
.panel{display:none}.panel.active{display:block}

/* Form */
.input-group{display:flex;gap:8px;margin-bottom:16px}
.input-group input,.input-group select{flex:1;padding:12px 16px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);color:var(--text);font-size:.95rem;outline:none;transition:.2s}
.input-group input:focus{border-color:var(--accent)}
.input-group select{max-width:120px;cursor:pointer}
button{padding:12px 24px;background:var(--accent);color:#fff;border:none;border-radius:var(--radius);font-weight:600;font-size:.9rem;cursor:pointer;transition:.2s;display:inline-flex;align-items:center;gap:6px}
button:hover{opacity:.9;transform:translateY(-1px)}
button:disabled{opacity:.5;cursor:not-allowed;transform:none}
button.secondary{background:var(--surface2);color:var(--text)}
button.secondary:hover{background:var(--border)}

/* Status */
.status{padding:12px 16px;border-radius:var(--radius);margin-bottom:16px;font-size:.9rem;display:none}
.status.error{display:block;background:rgba(255,92,108,.12);color:var(--red);border:1px solid rgba(255,92,108,.25)}
.status.loading{display:flex;align-items:center;gap:8px;background:rgba(124,92,255,.1);color:var(--accent);border:1px solid rgba(124,92,255,.2)}
.spinner{width:16px;height:16px;border:2px solid transparent;border-top-color:currentColor;border-radius:50%;animation:spin .6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* Results toolbar */
.toolbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px}
.toolbar .count{color:var(--muted);font-size:.85rem}
.toolbar .actions{display:flex;gap:6px}

/* Video detail card */
.detail-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;margin-bottom:20px}
.detail-card .thumb{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.detail-card .body{padding:20px}
.detail-card h2{font-size:1.2rem;margin-bottom:8px;line-height:1.3}
.detail-card .meta{display:flex;flex-wrap:wrap;gap:16px;color:var(--muted);font-size:.85rem;margin-bottom:12px}
.detail-card .meta span{display:flex;align-items:center;gap:4px}
.detail-card .desc{font-size:.9rem;color:var(--muted);line-height:1.5;white-space:pre-wrap;max-height:120px;overflow-y:auto}
.detail-card .tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.detail-card .tag{background:var(--surface2);padding:4px 10px;border-radius:20px;font-size:.78rem;color:var(--muted)}

/* Table */
.table-wrap{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--border)}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th{background:var(--surface2);padding:10px 12px;text-align:left;font-weight:600;color:var(--muted);text-transform:uppercase;font-size:.75rem;letter-spacing:.5px;white-space:nowrap}
td{padding:10px 12px;border-top:1px solid var(--border);max-width:300px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
tr:hover td{background:rgba(124,92,255,.04)}
.thumb-sm{width:80px;border-radius:4px}

/* Collected sidebar */
.collected-bar{position:fixed;bottom:0;left:0;right:0;background:var(--surface);border-top:1px solid var(--border);padding:12px 24px;display:none;align-items:center;justify-content:space-between;z-index:100}
.collected-bar.show{display:flex}
.collected-bar .info{color:var(--muted);font-size:.9rem}
.collected-bar .info strong{color:var(--green)}

@media(max-width:640px){
  .input-group{flex-direction:column}
  .input-group select{max-width:none}
  .toolbar{flex-direction:column;align-items:flex-start}
}
</style>
</head>
<body>
<div class="app">
  <header>
    <h1>YouTube Data Collector</h1>
    <p>Extract video metadata, search results &amp; channel data</p>
  </header>

  <div class="tabs">
    <div class="tab active" data-tab="video">Video Info</div>
    <div class="tab" data-tab="search">Search</div>
    <div class="tab" data-tab="channel">Channel</div>
    <div class="tab" data-tab="collected">Collected</div>
  </div>

  <!-- VIDEO -->
  <div class="panel active" id="panel-video">
    <div class="input-group">
      <input id="video-url" placeholder="Paste a YouTube video URL..." />
      <button id="btn-video">Extract</button>
    </div>
    <div id="video-status" class="status"></div>
    <div id="video-result"></div>
  </div>

  <!-- SEARCH -->
  <div class="panel" id="panel-search">
    <div class="input-group">
      <input id="search-query" placeholder="Search YouTube..." />
      <select id="search-count">
        <option value="5">5 results</option>
        <option value="10" selected>10 results</option>
        <option value="20">20 results</option>
        <option value="50">50 results</option>
      </select>
      <button id="btn-search">Search</button>
    </div>
    <div id="search-status" class="status"></div>
    <div id="search-result"></div>
  </div>

  <!-- CHANNEL -->
  <div class="panel" id="panel-channel">
    <div class="input-group">
      <input id="channel-url" placeholder="Paste a channel or playlist URL..." />
      <select id="channel-count">
        <option value="10">10 videos</option>
        <option value="30" selected>30 videos</option>
        <option value="50">50 videos</option>
        <option value="100">100 videos</option>
      </select>
      <button id="btn-channel">Fetch</button>
    </div>
    <div id="channel-status" class="status"></div>
    <div id="channel-result"></div>
  </div>

  <!-- COLLECTED -->
  <div class="panel" id="panel-collected">
    <div class="toolbar">
      <div class="count" id="collected-count">0 items collected</div>
      <div class="actions">
        <button class="secondary" onclick="exportData('csv')">Export CSV</button>
        <button class="secondary" onclick="exportData('json')">Export JSON</button>
        <button class="secondary" style="color:var(--red)" onclick="clearCollected()">Clear All</button>
      </div>
    </div>
    <div id="collected-result"></div>
  </div>
</div>

<div class="collected-bar" id="collected-bar">
  <div class="info"><strong id="bar-count">0</strong> items collected</div>
  <div class="actions">
    <button class="secondary" onclick="exportData('csv')">Export CSV</button>
    <button class="secondary" onclick="exportData('json')">Export JSON</button>
  </div>
</div>

<script>
const collected = [];

// Tabs
document.querySelectorAll('.tab').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(x => x.classList.remove('active'));
    t.classList.add('active');
    document.getElementById('panel-' + t.dataset.tab).classList.add('active');
    if (t.dataset.tab === 'collected') renderCollected();
  });
});

function setStatus(id, type, msg) {
  const el = document.getElementById(id);
  el.className = 'status ' + type;
  if (type === 'loading') el.innerHTML = '<div class="spinner"></div>' + msg;
  else el.textContent = msg;
  el.style.display = type ? (type === 'loading' ? 'flex' : 'block') : 'none';
}

function fmt(n) {
  if (n == null) return '—';
  return n.toLocaleString();
}

// Video
document.getElementById('btn-video').onclick = async () => {
  const url = document.getElementById('video-url').value.trim();
  if (!url) return;
  setStatus('video-status', 'loading', 'Extracting video data...');
  document.getElementById('video-result').innerHTML = '';
  try {
    const r = await fetch('/api/video', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({url})});
    const d = await r.json();
    if (d.error) throw new Error(d.error);
    setStatus('video-status', '', '');
    renderVideoDetail(d);
  } catch(e) { setStatus('video-status', 'error', e.message); }
};

function renderVideoDetail(d) {
  const el = document.getElementById('video-result');
  el.innerHTML = `
    <div class="detail-card">
      ${d.thumbnail ? `<img class="thumb" src="${d.thumbnail}" alt="">` : ''}
      <div class="body">
        <h2>${esc(d.title)}</h2>
        <div class="meta">
          <span>${esc(d.channel)}</span>
          <span>${fmt(d.views)} views</span>
          <span>${fmt(d.likes)} likes</span>
          <span>${d.duration_str || '—'}</span>
          <span>${d.upload_date || '—'}</span>
        </div>
        <div class="desc">${esc(d.description)}</div>
        ${d.tags.length ? `<div class="tags">${d.tags.slice(0, 15).map(t => `<span class="tag">${esc(t)}</span>`).join('')}</div>` : ''}
        <div style="margin-top:16px">
          <button onclick='addToCollected(${JSON.stringify(d).replace(/'/g, "&#39;")})'>Add to Collection</button>
          <a href="${d.url}" target="_blank" style="margin-left:12px;font-size:.9rem">Open on YouTube</a>
        </div>
      </div>
    </div>`;
}

// Search
document.getElementById('btn-search').onclick = async () => {
  const query = document.getElementById('search-query').value.trim();
  const count = document.getElementById('search-count').value;
  if (!query) return;
  setStatus('search-status', 'loading', 'Searching...');
  document.getElementById('search-result').innerHTML = '';
  try {
    const r = await fetch('/api/search', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({query, count})});
    const d = await r.json();
    if (d.error) throw new Error(d.error);
    setStatus('search-status', '', '');
    renderTable('search-result', d, true);
  } catch(e) { setStatus('search-status', 'error', e.message); }
};

// Channel
document.getElementById('btn-channel').onclick = async () => {
  const url = document.getElementById('channel-url').value.trim();
  const count = document.getElementById('channel-count').value;
  if (!url) return;
  setStatus('channel-status', 'loading', 'Fetching channel data...');
  document.getElementById('channel-result').innerHTML = '';
  try {
    const r = await fetch('/api/channel', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({url, count})});
    const d = await r.json();
    if (d.error) throw new Error(d.error);
    setStatus('channel-status', '', '');
    renderTable('channel-result', d, true);
  } catch(e) { setStatus('channel-status', 'error', e.message); }
};

function renderTable(containerId, rows, showAdd) {
  if (!rows.length) { document.getElementById(containerId).innerHTML = '<p style="color:var(--muted)">No results</p>'; return; }
  const el = document.getElementById(containerId);
  let html = `<div class="toolbar"><div class="count">${rows.length} results</div>`;
  if (showAdd) html += `<div class="actions"><button class="secondary" onclick='addAllToCollected(this)' data-rows='${JSON.stringify(rows).replace(/'/g, "&#39;")}'>Add All to Collection</button></div>`;
  html += `</div><div class="table-wrap"><table><thead><tr>`;
  if (rows[0].thumbnail) html += '<th></th>';
  html += '<th>Title</th><th>Channel</th><th>Views</th><th>Duration</th>';
  if (showAdd) html += '<th></th>';
  html += '</tr></thead><tbody>';
  for (const r of rows) {
    html += '<tr>';
    if (r.thumbnail) html += `<td><img class="thumb-sm" src="${r.thumbnail}" alt=""></td>`;
    html += `<td><a href="${r.url}" target="_blank">${esc(r.title)}</a></td>`;
    html += `<td>${esc(r.channel)}</td>`;
    html += `<td>${fmt(r.views)}</td>`;
    const dur = r.duration ? `${Math.floor(r.duration/60)}:${String(r.duration%60).padStart(2,'0')}` : '—';
    html += `<td>${dur}</td>`;
    if (showAdd) html += `<td><button class="secondary" style="padding:6px 12px;font-size:.8rem" onclick='addToCollected(${JSON.stringify(r).replace(/'/g, "&#39;")})'>+</button></td>`;
    html += '</tr>';
  }
  html += '</tbody></table></div>';
  el.innerHTML = html;
}

// Collection
function addToCollected(item) {
  if (collected.find(c => c.id === item.id)) return;
  collected.push(item);
  updateBar();
}

function addAllToCollected(btn) {
  const rows = JSON.parse(btn.dataset.rows);
  for (const r of rows) { if (!collected.find(c => c.id === r.id)) collected.push(r); }
  updateBar();
}

function updateBar() {
  const bar = document.getElementById('collected-bar');
  const cnt = document.getElementById('bar-count');
  cnt.textContent = collected.length;
  bar.classList.toggle('show', collected.length > 0);
  document.getElementById('collected-count').textContent = collected.length + ' items collected';
}

function renderCollected() {
  updateBar();
  if (!collected.length) {
    document.getElementById('collected-result').innerHTML = '<p style="color:var(--muted);text-align:center;padding:40px 0">No items collected yet. Use the other tabs to find and add videos.</p>';
    return;
  }
  renderTable('collected-result', collected, false);
}

function clearCollected() {
  collected.length = 0;
  updateBar();
  renderCollected();
}

async function exportData(fmt) {
  if (!collected.length) return;
  try {
    const r = await fetch('/api/export', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({data: collected, format: fmt})
    });
    const blob = await r.blob();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'youtube_data.' + fmt;
    a.click();
  } catch(e) { alert('Export failed: ' + e.message); }
}

function esc(s) { if (!s) return ''; const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

// Enter key support
document.getElementById('video-url').addEventListener('keydown', e => { if (e.key === 'Enter') document.getElementById('btn-video').click(); });
document.getElementById('search-query').addEventListener('keydown', e => { if (e.key === 'Enter') document.getElementById('btn-search').click(); });
document.getElementById('channel-url').addEventListener('keydown', e => { if (e.key === 'Enter') document.getElementById('btn-channel').click(); });
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

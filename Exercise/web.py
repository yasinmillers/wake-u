import requests
import bs4

base_url = "https://xkcd.com"
url = "https://xkcd.com/1"

while "#" not in url: 
   # PART 1 - Request and Soupify ---------
   # Request the Web Page
   response = requests.get(url)
   # Parse the page to make it easy to use
   soup = bs4.BeautifulSoup(response.content, "html.parser")

   # PART 2 - Find the URL of the img ----------
   img_element = soup.select("#comic img")[0]
   img_src = img_element["src"]
   img_src = "http:" + str(img_src)

   # Get the name of the file
   img_name = img_src.split("/")[-1]

   # PART 3 - Download the Comic -------------
   response = requests.get(img_src)

   with open("comics/" + img_name,'wb') as file: 
        file.write(response.content) 
   
   next_a = soup.select(".comicNav a[rel='next']")[0]
   next_href = next_a["href"]
   url = base_url + str(next_href)
   print(url)
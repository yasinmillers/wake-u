import socket
def create_socket(host='localhost', port=8080):
    """Create a TCP socket and connect to the specified host and port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    return s
print("Socket created and connected to {}:{}".format('localhost', 8080))   
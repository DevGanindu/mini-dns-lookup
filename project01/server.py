import socket

host = "127.0.0.1"  
port = 20001       
buffer_size = 1024  


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((host, port))
print(f"UDP Server is running and listening on {host}:{port}...\n")

while True:
    message_bytes, client_address = server_socket.recvfrom(buffer_size)
    
    domain_name = message_bytes.decode()
    print(f"Client asked for the IP of: {domain_name}")
    
    try:
        resolved_ip = socket.gethostbyname(domain_name)
        print(f"Success! Sending back: {resolved_ip}\n")
    except socket.gaierror:
        resolved_ip = "Error: Domain not found"
        print("Failed to find domain. Sending error message.\n")
        
    server_socket.sendto(resolved_ip.encode(), client_address)

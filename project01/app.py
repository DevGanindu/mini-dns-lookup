from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None
    
    if request.method == 'POST':
        domain_to_search = request.form['domain']
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(2.0) 
        
        try:
            client_socket.sendto(domain_to_search.encode(), ('127.0.0.1', 20001))
            
            response_bytes, _ = client_socket.recvfrom(1024)
            answer = response_bytes.decode()
            
        except socket.timeout:
            answer = "Error: Background UDP Server is offline."
        finally:
            client_socket.close()
            
    return render_template('index.html', result=answer)

if __name__ == '__main__':
    print("Starting Web Interface on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
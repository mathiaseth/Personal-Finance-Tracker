from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import json

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/', '/index.html']:
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/api/transactions':
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            print("Received POST data:", post_data)
            self.send_response(201)
            self.end_headers()
            response = {'status': 'Transaction added'}
            self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        return  # Suppress console messages

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    os.chdir('C:\\Users\\mathias\\Downloads\\work\\VSCode\\Personal Finance Tracker')  # Correct path to your HTML/JS files
    httpd.serve_forever()
    #using http://localhost:8000/

if __name__ == '__main__':
    run()

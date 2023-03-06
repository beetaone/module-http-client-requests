from http.server import HTTPServer, BaseHTTPRequestHandler


class TokenChecker(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_PUT(self):
        length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(length).decode()
        print(f"Received payload: {payload}")
        self.handle_request()

    def do_DELETE(self):
        self.handle_request()

    def handle_request(self):
        # Extract the authorization token from the header
        auth_header = self.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(' ')[1]
        else:
            auth_token = None

        # Check if the token is valid
        if auth_token == '1234567890abcdef':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Authorization successful')
        else:
            self.send_response(401)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Authorization failed')


# Start the server
PORT = 8081
server = HTTPServer(('', PORT), TokenChecker)
print(f"Serving on port {PORT}")
server.serve_forever()

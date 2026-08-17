from database_api import SQLite
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

db = SQLite(r"C:\Users\hiwot\Git projects\Database\mystore.db")


class LoginHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/login":
            self.send_response(404)
            self.end_headers()
            return
        #read the request body

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode()
        data = json.loads(body)

        username = data.get("username")
        password = data.get("password")

        query = "SELECT * FROM users WHERE username=? AND password=?"
        args = (username,password)
        result = db.execute_query(query, args)
        if len(result) > 0:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Login Success")
        else:
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"Login Failure")

if __name__ == "__main__":
    #start http server
    port = 8080
    httpd = HTTPServer(("", port), LoginHandler)
    print(f"Serving on  http://localhose:{port}")
    httpd.serve_forever()
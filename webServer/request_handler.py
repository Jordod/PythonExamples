from http.server import BaseHTTPRequestHandler
from datetime import date
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

        smth = {
            "_path": self.path,
            "date": str(date.today()),
        }

        self.wfile.write(bytes(json.dumps(smth), "utf-8"))

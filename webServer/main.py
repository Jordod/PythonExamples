from http.server import HTTPServer
import request_handler

host = "localhost"
port = 8080

if __name__ == "__main__":
    server = HTTPServer((host, port), request_handler.Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
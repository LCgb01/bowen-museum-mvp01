from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import time

class MuseumAPIHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "status": "running",
                "service": "Museum AI Guide",
                "server_ip": "8.163.20.239",
                "timestamp": time.time(),
                "endpoints": {
                    "frontend": "http://8.163.20.239:8080",
                    "api": "http://8.163.20.239:8000"
                }
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            # 默认行为：提供文件服务
            super().do_GET()

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MuseumAPIHandler)
    print("博物馆API服务启动在端口8000...")
    httpd.serve_forever()

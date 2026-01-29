from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

class MuseumHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "status": "running",
                "service": "博闻AI博物馆API",
                "server_ip": "8.163.20.239",
                "timestamp": time.time(),
                "version": "1.0.0"
            }
            self.wfile.write(json.dumps(response).encode())
            
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy"}).encode())
            
        elif self.path == '/api/exhibits':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            exhibits = [
                {"id": 1, "name": "古代文物", "description": "展示古代文明的遗物"},
                {"id": 2, "name": "现代艺术", "description": "当代艺术家的作品展示"},
                {"id": 3, "name": "AI互动区", "description": "人工智能与艺术的结合"}
            ]
            self.wfile.write(json.dumps(exhibits).encode())
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())
    
    def log_message(self, format, *args):
        # 禁用默认日志输出
        pass

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MuseumHandler)
    print("博物馆API服务启动在端口8000...")
    httpd.serve_forever()

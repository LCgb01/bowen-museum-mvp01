#!/bin/bash
echo "=== 博物馆AI系统部署 ==="
echo "时间: $(date)"
echo "服务器IP: 8.163.20.239"

# 1. 停止并删除旧容器
echo "清理旧容器..."
docker stop museum-frontend museum-backend 2>/dev/null || true
docker rm museum-frontend museum-backend 2>/dev/null || true

# 2. 启动前端容器（Nginx）
echo "启动前端服务 (Nginx)..."
docker run -d \
  --name museum-frontend \
  --restart unless-stopped \
  -p 8080:80 \
  -v /var/www/museum-guide/html:/usr/share/nginx/html:ro \
  nginx:alpine

# 3. 启动后端容器（Python API）- 修复：使用正确的启动命令
echo "启动后端API服务 (Python)..."
docker run -d \
  --name museum-backend \
  --restart unless-stopped \
  -p 8000:8000 \
  -v /var/www/museum-guide/api:/app \
  python:3.9-slim \
  sh -c "cd /app && pip install -r requirements.txt 2>/dev/null || echo 'No requirements.txt' && python3 server.py"

# 4. 等待服务启动
echo "等待服务启动..."
sleep 8

# 5. 验证部署
echo "=== 验证部署 ==="
echo "前端状态 (8080):"
curl -s -o /dev/null -w "HTTP状态码: %{http_code}\n" http://localhost:8080

echo "后端状态 (8000):"
curl -s -o /dev/null -w "HTTP状态码: %{http_code}\n" http://localhost:8000

echo ""
echo "✅ 部署完成！"
echo "🌐 访问地址:"
echo "前端页面: http://8.163.20.239:8080"
echo "API接口: http://8.163.20.239:8000"
echo "API健康检查: http://8.163.20.239:8000/health"
echo "API展览数据: http://8.163.20.239:8000/api/exhibits"
echo ""
echo "📊 容器状态:"
docker ps --filter "name=museum" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

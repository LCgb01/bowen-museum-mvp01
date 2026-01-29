#!/bin/bash
echo "=== Museum AI Guide Deployment ==="
echo "Time: $(date)"

# 停止旧容器
docker stop museum-web 2>/dev/null || true
docker rm museum-web 2>/dev/null || true

# 启动新容器
docker run -d \
  --name museum-web \
  -p 8080:80 \
  -p 8000:8000 \
  -v /var/www/museum-guide:/app \
  -w /app \
  python:3.9-slim \
  sh -c "apt-get update && apt-get install -y nginx && \
         echo 'Museum AI Guide - $(date)' > /app/index.html && \
         nginx -g 'daemon off;' & \
         python3 -m http.server 8000"

echo "=== 部署完成 ==="
echo "Frontend: http://8.163.20.239:8080"
echo "API: http://8.163.20.239:8000"

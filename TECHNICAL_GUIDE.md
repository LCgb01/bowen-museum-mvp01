# 博闻AI博物馆系统 - 技术开发指南

## 服务器信息
- IP: 8.163.20.239
- 主机名: iZ7xvimodj90yqjzlqim0lZ
- SSH用户: root
- 操作系统: Ubuntu 22.04

## 服务端口
- 8080: 前端Web服务
- 8000: 后端API服务
- 22: SSH管理端口

## 目录结构
/var/www/museum-guide/
├── html/           # 前端静态文件
├── api/            # 后端API代码
├── docker/         # Docker配置文件
├── scripts/        # 部署脚本
└── data/           # 数据文件

## 部署命令
1. 快速重启: docker restart museum-web
2. 查看日志: docker logs museum-web
3. 完整部署: bash /root/museum-deploy.sh

## GitHub集成
- SSH公钥已生成: /root/.ssh/id_rsa.pub
- 需要添加到GitHub仓库的Deploy keys

## 系统状态检查
bash /root/check-status.sh

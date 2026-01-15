# API 接口文档

## 基础信息
- 开发环境地址：`http://localhost:8000`
- 在线API文档：`http://localhost:8000/docs` (Swagger UI)

## 文物管理接口

### 1. 创建文物
**POST** `/artifacts/`

**请求体示例**：
```json
{
  "artifact_id": "001",
  "name": "青铜鼎",
  "era": "商代",
  "museum": "中国国家博物馆",
  "images": ["http://example.com/image1.jpg"],
  "summary": "30字精华介绍",
  "standard": "300字标准讲解",
  "deep": "1000字深度解读",
  "stories": [{"title": "故事标题", "content": "故事内容"}],
  "keywords": ["青铜器", "礼器"]
}

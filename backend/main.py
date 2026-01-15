from fastapi import FastAPI
from backend.api import artifacts, upload  # 导入路由
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="博闻AI博物馆导览API")

# 配置跨域，方便前端调试
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应限制为具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(artifacts.router)
app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "博闻AI博物馆导览后端服务运行中"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

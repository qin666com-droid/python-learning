"""
响应: 响应客户端请求,返回服务器端处理结果

响应类型设置方式:
    装饰器中指定响应类:固定返回类型(HTML,纯文本等)
    返回响应对象:文件下载,图片,流失响应

"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")

async def root():
    return {"msg":"Hello World"}

#接口: 返回一张图片
@app.get("/file")
async def file():
    photo = "./photoes/img.png"
    return FileResponse(photo)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

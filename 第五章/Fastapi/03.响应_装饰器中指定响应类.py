"""
响应: 响应客户端请求,返回服务器端处理结果

响应类型设置方式:
    装饰器中指定响应类:固定返回类型(HTML,纯文本等)
    返回响应对象:文件下载,图片,流失响应

"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Hello World"}

#接口 -> 响应 HTML 代码
@app.get("/html",response_class=HTMLResponse)
async def html():
    return "<h1>This is 一级标题</h1>"


if __name__ =="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)





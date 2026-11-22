"""
中间件
中间件: 用于在请求处理过程中,对请求进行拦截,并进行处理,
       最后再将处理后的响应返回给客户端。
步骤:
    1. 导入FastAPI类
    2. 定义路由函数,并使用@app.get装饰器装饰
    3. 在路由函数中,添加中间件代码
    4. 运行FastAPI应用
"""
from urllib import response

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.middleware("http")
async def middleware(request,call_next):
    print('中间件1 start')
    response = await call_next(request)
    print('中间件1 end')
    return response

@app.middleware("http")
async def middleware2(request,call_next):
    print('中间件2 start')
    response = await call_next(request)
    print('中间件2 end')
    return response

@app.middleware("http")
async def middleware3(request,call_next):
    print('中间件3 start')
    response = await call_next(request)
    print('中间件3 end')
    return response



@app.get("/")
async def  root():
    return {"msg":"Hello World"}



if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)




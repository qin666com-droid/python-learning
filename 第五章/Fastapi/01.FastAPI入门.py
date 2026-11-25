import uvicorn
from fastapi import FastAPI

# 创建FastAPI应用实例
app = FastAPI()


#定义API接口 --> 该函数的返回值表示API接口 的返回值的数据,接口访问路径为 /,请求方式为 GET
@app.get("/")
def read_root():
    return {"Hello": "World "}

#定义API接口
# @app.get("/users")
# def get_users():
#     return [
#         {"id": 1, "name": "张三"},
#         {"id": 2, "name": "李四"},
#     ]

#访问 /hello 响应结果 msg: 你好 FastAPI
# @app.get("/hello")
# async def get_hello():
#     return {"msg":"你好 FastAPI"}

#练习:访问路径/user/hello,响应结果是{"msg":"我正在学习fastapi..."}

@app.get("/user/hello")
async def get_learning():
    return {"msg": "我正在学习fastapi..."}


#启动服务 ---> uvicorn: python中的轻量级web服务器
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)






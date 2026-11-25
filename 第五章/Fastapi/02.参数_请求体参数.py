"""
案例: 参数之请求体参数
BaseModel: 基础模型,用于定义请求体参数的结构  -->pydantic
Field: 字段,用于定义请求体参数的字段,
并添加额外的信息,如必填、默认值等  -->pydantic.Field


"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Hello World"}


#注册: 用户名和密码  -> str
class User(BaseModel):
    username: str = Field(default = "扶苏",min_length=2, max_length=10, description="用户名")
    password: str = Field(min_length=3,max_length=10, description="密码")

@app.post("/login")
async def login(user: User):
    return user




#练习1: 设计接口新增图书,图书信息包含: 书名,作者,出版社,售价
# class Books(BaseModel):
#     name: str
#     author: str
#     publisher: str
#     price: float
#
# @app.post("/book")
# async def add_books(book: Books):
#     return book





#练习2: 设计接口新增图书,图书信息包含: 书名,作者,出版社,售价
"""
要求:
    书名:不能为空;长度2-20
    作者:长度2-10
    出版社:默认值为"扶苏出版社"
    售价:不能为空;必须为浮点数;必须大于0
"""
class Books(BaseModel):
    name: str = Field(..., min_length=2, max_length=20, description="书名")
    author: str = Field(min_length=2, max_length=10, description="作者")
    publisher: str = Field(default="扶苏出版社", description="出版社")
    price: float = Field(..., gt=0, description="售价")

@app.post("/books")
async def books(book: Books):
    return book








if __name__ =="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




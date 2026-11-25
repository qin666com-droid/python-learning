"""
案例: 参数之路径参数


path参数: 路径参数


"""
import uvicorn
from fastapi import FastAPI,Path
#创建FastAPI应用实例 app
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
#定义API接口,请求路径为 /book/{id},请求方式为 GET
# @app.get("/book/{id}")
# async def get_book(id:int):
#     return {"id":id,"title":f'这是第{id}本书'}

#类型注解:Path参数
# @app.get("/book/{id}")
# async def get_book(id:int=Path(...,gt =0,lt=101,description="图书ID,取值范围为1-100")):
#     return {"id":id,"title":f'这是第{id}本书'}

#需求: 查找书籍的作者,路径参数 name,长度范围 2-10
# @app.get("/author/{name}")
# async def get_author(name:str = Path(...,min_length=2,max_length=10,description="作者姓名,长度范围为2-10个字符")):
#     return {"author":name}






#练习1:以用户id为路径参数设计URL,要求响应结果包含用户id和名称
# @app.get("/user/{id}")
# async def get_user(id:str):
#     return {"id": id,"name":f'用户的名称为{id}'}

#练习2:以 新闻分类id为参数设计URL,id范围为1-100
#     以 新闻分类名称为参数设计URL,分类名称长度为2-10
@app.get("/user/{id}/{name}")
async def get_news(id:int = Path(...,gt =0,lt=101,description="新闻分类ID,取值范围为1-100"),
                    name:str = Path(...,min_length=2,max_length=10,description="新闻分类名称,长度范围为2-10个字符")):
    return {"msg":f'这是第{id}个新闻分类,名称为{name}'}





#启动FastAPI应用,监听IP地址为 127.0.0.1,端口号为 8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)





"""
案例: 参数之查询参数

query参数: 查询参数(URL参数)

"""
# from idlelib.query import Query

import uvicorn
from fastapi import FastAPI,Query

#创建FastAPI应用实例 app
app = FastAPI()

#定义API接口
@app.get("/")
async def root():
    return {"msg":"Hello World"}

#需求: 查询新闻-->分页,skip: 跳过的记录数,  limit: 返回的记录数 10
# @app.get("/news/news_list")
# async def get_news_list(
#         skip: int = Query(0,description="跳过的记录数"),
#         limit: int = Query(10,description="返回的记录数")
# ):
#     return {"skip":skip,"limit":limit}



#练习:设计接口查询图书,要求携带两个查询参数:图书分类和价格
#图书分类: 默认值为python开发,长度限制5-255;价格:限制大小范围50-100
@app.get("/books/books_list|books_price")
async def get_books(
        category: str = Query("python开发",min_length=5,max_length=255,description="图书分类"),
        price: int =Query(...,gt=50,lt=100,description="图书价格,取值范围为50-100")
):
    return {"category":category,"price":price}




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


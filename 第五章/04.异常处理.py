"""
异常处理
HTTPException: 用于处理HTTP异常，例如404、500等。
步骤:
    1. 导入HTTPException类
    2. 定义路由函数,并使用@app.get装饰器装饰
    3. 在路由函数中,判断id是否在id_list中,如果不在,则抛出HTTPException异常
    4. 如果在,则返回id,title,content字段

"""
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Hello World"}

#需求: 按 id 查询新闻 -> 1-6
@app.get("/news/{id}")
async def get_news(id: int):
    id_list = [1,2,3,4,5,6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="新闻不存在")
    return {"id": id, "title": f'这是第{id}条新闻', "content": f'这是条有用的内容'}




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)






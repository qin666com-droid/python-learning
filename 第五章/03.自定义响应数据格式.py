from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Hello World"}

#需求: 新闻接口 -> 响应数据格式 : id,title, content
class News(BaseModel):
    id: int
    title: str
    content: str

@app.get("/news/{id}",response_model=News)  # 定义响应数据格式为News类,并返回id,title,content,不能返回其他字段或者缺少字段,否则会报错
async def news(id: int):
    return {
        "id": id,
        "title": f'这是第{id}条新闻',
        "content": f'这是条有用的内容'
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




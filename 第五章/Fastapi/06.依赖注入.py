"""
依赖注入:
    依赖注入是一种设计模式,用于在应用程序中解耦组件之间的依赖关系。
    它通过将组件的依赖关系从代码中分离出来,将依赖关系作为参数传递给组件,
    从而实现组件的解耦和可维护性。
    依赖注入可以用于注入服务、数据库连接、配置等,使组件更加独立和可测试。
步骤:
    1.定义依赖项
    2.导入Depends依赖项
    3.声明依赖项在路由函数中 -> 依赖注入
"""

import uvicorn
from fastapi import FastAPI,Query,Depends  #2.导入Depends依赖项

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

# 分页参数逻辑共用: 新闻列表和用户列表

# 1.定义依赖项
async def common_parameters(
        skip: int = Query(0,ge = 0),
        limit: int = Query(10,le = 60)
):
    return {"skip":skip,"limit":limit}








#3.声明依赖项在路由函数中 -> 依赖注入
@app.get("/news/news_list")
async def get_news_list(common = Depends(common_parameters)):
    return common


@app.get("/user/user_list")
async def get_user_list(common = Depends(common_parameters)):
    return common

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

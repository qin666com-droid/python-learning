"""
案例: 基于传入的数值(每批次的歌词条数), 创建 生成器 ,生成批次歌词

"""
import math
# 需求: 基于文件中的歌词,创建生成器,根据传入的数值(每批次的歌词条数), 生成批次歌词
#1. 定义函数,接收 每批次的歌词条数,并返回 生成器
def dataset_loader(batch_size):
    """
    自定义的 歌词 批量生成器
    :param batch_size: 每批次的歌词条数
    :return: 生成器,每个元素都是一批次的歌词,例如: (8条,8条,...)
    """
    # 1.1 读取文件中的歌词
    with open("data/eason.txt", "r", encoding="utf-8") as f:
        # 1.2 一次读取所有行
        lyrics = f.readlines()

        # 1.3 计算批次总数,假设 : 5批
        total_batch = math.ceil(len(lyrics) / batch_size)

        # 1.4 for循环方式,获取到每批次的数据,放到生成器中,并返回
        for idx in range(total_batch):         #idx的值: 0,1,2,3,4
            # 第一批歌词,批次索引(idx = 0),歌词为: 第1条-第8条,索引为: 0-7
            # 第二批歌词,批次索引(idx = 1),歌词为: 第9条-第16条,索引为: 8-15
            # 第三批歌词,批次索引(idx = 2),歌词为: 第17条-第24条,索引为: 16-23
            # 第四批歌词,批次索引(idx = 3),歌词为: 第25条-第32条,索引为: 24-31
            # 第五批歌词,批次索引(idx = 4),歌词为: 第33条-第40条,索引为: 32-39
            yield lyrics[idx * batch_size: idx * batch_size + batch_size]



#2. 测试
dl =dataset_loader(3)
print(next(dl))     # 第一批歌词
print(next(dl))     # 第二批歌词
print(next(dl))     # 第三批歌词

# for batch_data in dl:
#     print(batch_data)

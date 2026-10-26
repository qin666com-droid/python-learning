#导包
import json
#
# #写入json数据文件
# user = {
#     "name": "坤",
#     "age": 18,
#     "gender": "男",
#     "hobby": [
#         "足球",
#         "篮球",
#         "跑步"
#     ]
# }
# with open("recources/users.json", "w", encoding="utf-8") as f:
#     #ensure_ascii=False 表示不使用转义字符,直接写入中文
#     #ensure_ascii: 默认值为True, 确保输出的数据都是ascii码(非ascii码会使用转义字符表示)
#     #indent=4 表示缩进4个空格
#     #indent : 会在输出的json数据中添加换行符,使数据更易读
#     json.dump(user, f, ensure_ascii=False, indent=4)


#读取json数据文件
with open("recources/users.json", "r", encoding="utf-8") as f:
    #load()方法会将json数据转换为python对象(字典)
    user = json.load(f)
    print(user)
    print((type(user)))




















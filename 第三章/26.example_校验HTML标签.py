r"""
案例 : 演示正则表达式之 校验qq号

正则规则:
      |      或, 匹配多个正则表达式中的任意一个字符
        ()     代表 分组,从左往右数,第几个左小括号(, 就是第几个分组
        \()    取消括号的特殊意义, 就是一个普通的括号
        \num   匹配括号中的内容,引用第几组的内容

        扩展:
            (?P<组名>)  代表匹配括号中的内容,并将其命名为组名,设置分组
            (?P=组名)  代表引用组名, 与括号中的内容进行匹配,使用分组

"""
import re
from unittest import result

#需求: 校验html的单极标签
# #1.定义html标签
# html_s = '<html>我是html标签</html>'        #字母数:1-4
#
# #2. 校验匹配
# #写法1:重新copy一份
# result = re.match(r'<([a-zA-Z0-9]{1,4})>.*</[a-zA-Z0-9]{1,4}>', html_s)
#
# #写法2:引入分组概念
# # result = re.match(r'<([a-zA-Z0-9]{1,4})>.*</\1>', html_s)
#
#
# #3.打印结果
# if result:
#     print(result.group())
# else:
#     print('html标签不合法')

#需求2: 校验html的单极标签
# #1.定义html标签
html_s = '<html><h1>我是html标签</h1></html>'        #字母数:1-4   标题标签:1-6

# #2. 校验匹配
#写法1:重新copy一份
# result = re.match(r'<[a-zA-Z]{1,4}><h[1-6]>.*</h[1-6]></[a-zA-Z]{1,4}>', html_s)

#写法2:引入分组概念
result = re.match(r'<([a-zA-Z]{1,4})><h[1-6]>.*</h[1-6]></\1>', html_s)

#写法3:使用扩展规则
result = re.match(r'<(?P<标签>[a-zA-Z]{1,4})><h[1-6]>.*</h[1-6]></(?P=标签)>', html_s)

#3.打印结果
if result:
    print(result.group())
else:
    print('html标签不合法')

r"""
案例 : 演示正则表达式之 校验邮箱

正则规则:
      |      或, 匹配多个正则表达式中的任意一个字符
        ()     代表 分组,从左往右数,第几个左小括号(, 就是第几个分组
        \()    取消括号的特殊意义, 就是一个普通的括号
        \num   匹配括号中的内容,引用第几组的内容

        扩展:
            (?P<组名>)  代表匹配括号中的内容,并将其命名为组名,设置分组
            (?P=组名)  代表引用组名, 与括号中的内容进行匹配,使用分组

"""
import email
#导包
import re
from unittest import result

#1.定义邮箱
email = '1235@qq.com'

#2. 校验邮箱是否合法
result = re.match(r'[a-zA-Z_0-9]{4,20}@(163|123|qq)\.com', email)

#3.打印结果
if result:
    print(f'合法邮箱为 {email}')
    print(f'合法邮箱为 {result.group(0)}')   #获取整个匹配结果
    print(f'邮箱的用户名为 {result.group(1)}')   #获取第1分组的内容

else:
    print('邮箱不合法')

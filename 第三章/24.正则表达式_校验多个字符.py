"""
案例: 演示正则表达式之 检验多个字符

正则表达式介绍:
    概述:
        正确的, 符合特定规则的 字符串
        Regular Expression, 正则表达式, 正则, 正则匹配,简称: re

    细节:
        1. 学正则表达式, 就是学正则表达式的规则
        2. 能用讲的规则,看懂式子,并简单修改
        3. 正则不独属于Python, 也是其他语言的语法, 例如: Java, C# 等

    步骤:
        1. 导包
            import re
        2. 正则匹配
            result = re.match(正则表达式,字符串)    从前向后匹配,只要能匹配即可
            result = re.search(正则表达式,字符串)    分段匹配,只要能匹配即可,就返回第一个匹配结果
        3. 获取匹配结果
            result.group()
    正则常用的规则:
        .      匹配任意字符,除了 换行符 \n
        \.     取消.的特殊意义, 就是一个普通的.
        a      匹配字母a
        [abc]  代表匹配字母a,b,c中的任意一个
        [^abc] 代表除了字母a,b,c中的其他任意一个字符
        \d     代表匹配任意数字,等价于 [0-9]
        \D     代表匹配任意非数字,等价于 [^0-9]
        \W     代表匹配任意非字母数字下划线,等价于 [^a-zA-Z0-9_]
        \s     代表匹配任意空格,等价于 [ \t\n\r\f\v]
        \S     代表匹配任意非空格,等价于 [^ \t\n\r\f\v]
        \w     代表匹配任意字母,数字, 下划线,等价于 [a-zA-Z0-9_]

        ^      匹配字符串的开头
        $      匹配字符串的结尾

        *      匹配任意多个字符,包括0个字符,>=0
        +      匹配任意多个字符,不包括0个字符,>=1
        ?      匹配0个或1个字符
        {n}    匹配n个字符
        {n,m}  匹配n到m个字符

        |      或, 匹配多个正则表达式中的任意一个字符
        ()     括号, 代表匹配括号中的正则表达式
        \()    取消括号的特殊意义, 就是一个普通的括号
        \num   匹配括号中的内容

        扩展:
            (?P<组名>)  代表匹配括号中的内容,并将其命名为组名
            (?P=组名)  代表引用组名, 与括号中的内容进行匹配



"""
# 导包
import re
from unittest import result

# 验证
# *               匹配任意多个字符, 包括0个字符, >= 0
result = re.match(r'.*', 'hello world')        # 匹配成功
result = re.match(r'.*qkw', 'hello qkw')        # 匹配成功
# +               匹配任意多个字符, 不包括0个字符, >= 1
result = re.match(r'.+', 'hello world')        # 匹配成功
result = re.match(r'.+qkw', 'hello qkw')        # 匹配成功

# ?               匹配0个或1个字符
result = re.match(r'.?', 'hello world')     # 匹配成功
result = re.match(r'.?qkw', '6qkw')         # 匹配成功

# {n}             匹配n个字符
result = re.match(r'\d{3}qkw\w{3,6}', '123qkw67890')     # 匹配成功
result = re.match(r'\d{3}qkw\w{3,6}', '123qkw67$')      # 失败
result = re.match(r'\d{3}qkw\w{3,6}', '123qkw678$')     # 匹配成功

# {n, m}          匹配n到m个字符
result = re.match(r'\d{3,6}qkw\w{3,6}', '123qkw67890')     # 匹配成功
result = re.match(r'\d{3,6}qkw\w{3, 6}', '123qkw673$')      # 失败,注意空格
result = re.match(r'\d{3,6}qkw\w{3,6}', '123qkw678$')     # 匹配成功


#查看结果
print(result.group() if result else '未匹配到')









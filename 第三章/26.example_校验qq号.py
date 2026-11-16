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

#需求: 数据格式为 qq:数字, 从中提取qq文本 和 qq号

#1.定义qq号
q = 'qq:2507311144'

#2. 校验qq号是否合法
result = re.match(r'(qq):(\d+)', q)


#3.打印结果
if result:
    print(result.group())
    print(result.group(0))  #效果同上
    print('-'*30)
    print(result.group(1))
    print(result.group(2))


else:
    print('qq号不合法')

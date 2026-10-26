# 常见数据类型 -->
# type () 获取指定的字面量或变量的类型
# print(type("hello world"))
# print(type(10))
# print(type(3.14))
# print(type(True))
# print(type(None))
#
# num = 36
# print(type(num))
# 常见数据类型 -->isinstance(数据,类型)
#--> bool值 --> 判定数据是否是指定的类型,是:True;否则:False
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))

# # 字符串
# # 定义字符串的三种方式
# s1 = "hello" #双引号
# s2 = 'python ' #单引号
# s3 = """
# hello:
# 欢迎大家开始学习python
# """ # 三引号 (多行字符串)
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# #定义字符串-->It's good
# # 转义字符 \'  \"  \n  \t
# msg = 'It\'s good '
# print(msg)
# msg2 = "It's good "
# print(msg2)
# msg3 = "hello 的意思是 \"您好\" "
# print(msg3)
# print("\t欢迎来到青苹果乐园!\n\t玩得开心点!")#\n换行  \t缩进

#字符串拼接
# s1 = "人生苦短" "多去走走"
# print(s1)
# msg1 = "人生苦短"
# msg2 = "多去走走"
# print("邱叔说:" +msg1+","+msg2)
#
# #案例  -->str(int数字) -->将int类型的数字转为字符串
# name = "邱邱"
# age = 22
# pro = "软件工程"
# hobby = "python,java"
# print("大家好,我是"+name+",今年"+str(age)+"岁,学习的专业是"+pro+",爱好"+hobby)

#字符串格式化 -->方式一 %s 占位符
# name = "邱邱"
# age = 22
# pro = "软件工程"
# hobby = "python,java"
# print("大家好,我是 %s,今年 %s 岁,学习的专业是 %s ,爱好 %s" %(name,age,pro,hobby))


#字符串格式化 -->方式二 f"..{变量/表达式}.." -->推荐方式
name = "邱邱"
age = 22
pro = "软件工程"
hobby = "python,java"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")


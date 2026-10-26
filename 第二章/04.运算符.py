# #  算术运算符 :+ - * / // % **
# print("5+2=",5+2) # 加
# print("5-2=",5-2) # 减
#
# print("5*2=",5*2) # 乘
# print("5/2=",5/2) # 除(结果保留小数)
# print("5//2=",5//2)  # 整除(结果为整数)
# print("5%2=",5%2)  # 取余/求模
# print("5**2=",5**2) # 幂指数.5 的 2次方
#
#
# # 算术运算符的优先级 --> ** -->* / // % --> + -
# print("5+2/3**2=",5+2/3**2)


# 案例 输入x与y,计算和与差
# x = input("输入值")
# y = input("输入值")
# print(f"输出和{float(x)+float(y)}")
# print(f"输出差{float(x)-float(y)}")

 # 案例1.计算输入三个整数的平均值
# a  = int(input("输入整数:"))
# b  = int(input("输入整数:"))
# c  = int(input("输入整数:"))
# print("(a+b+c)/3",(a+b+c)/3)


 # 案例二.要求输入梯形的上底,下底,高,然后计算梯形的面积
# d1 = float(input("输入梯形的上底:"))
# d2 = float(input("输入梯形的下底:"))
# h  = float(input("输入梯形的高:"))
# print("(d1+d2)*h/2",(d1+d2)*h/2)
 # 案例3.要求输入圆的半径,然后计算圆的周长和面积

# r = float(input("输入圆的半径:"))
# print(f"圆的周长:{2*3.14*r }")
# print(f"圆的面积:{3.14*r*r  }")

 # 案例4.身体质量BMI的计算(BMI = 体重(kg) /身高(m)^2)
 # 输入体重(单位kg),输入身高(单位m),计算BMI并输出
# wei = float(input("输入体重:"))
# hig = float(input("输入身高:"))
# print(f"BMI={wei/hig**2}")



# 赋值运算符: = += -= *= /= //= %= **=
# num = 36
#
# num += 10
# print("num +=10后,num=",num) #46
#
# num -= 10
# print("num -=10后,num=",num) #36
#
# num *= 10
# print("num *=10后,num=",num) #360
#
# num /= 10
# print("num /=10后,num=",num) #36.0
#
# num //=10
#
# print("num //=10后,num=",num) #3.0
#
# num %= 10
# print("num %=10后,num=",num) #3.0
#
# num **= 10
# print("num **=10后,num=",num)




# 比较运算符: == != > >= < <=
# print("521 == 521 ?",521 ==521) #True
# print("'521' == '521' ?",'521' =='521') #True
# print("521 != 521 ?",521 !=521) #False
#
# print("521 > 521 ?",521 >521) #False
# print("521 >= 521 ?",521 >= 521) #True
#
# print("521 < 521 ?",521 < 521)  #False
# print("521 <= 521 ?",521 <= 521) #True

#逻辑运算符 : and or not
# #案例1:输入一个整数,判断是否在10-20间
# num = int(input("输入一个整数:"))
# print(f"{num}在10-20之间", num >=10 and num <=20)
# print(f"{num}在10-20之间", 10 <= num <= 20)
# and 连接的条件是并且的关系,两个条件同时成立,结果才为True

#案例2:输入一个整数,判断是否不在10-20之间
n =int(input("输入一个整数:"))
print(f"{n}不在10-20之间:",n < 10 or n > 20)



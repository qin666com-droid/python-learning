"""
案例2:猜数字游戏
    1.系统随机生成应该数字

    2.用户根据提示猜数字,并将其所猜的数字输入系统
    3.若猜错,系统给出提示是猜大了还是猜小了,然后继续输入猜的数字
    4.若猜对,系统自动退出,游戏结束
import random
random_num = random.randint(1, 100) #生成随机数

while True:
#比较
    num =int(input("请输入一个数字:"))
    if num > random_num:
        print("输入的数字太大了!请重新输入!!!")
    elif num < random_num:
        print("输入的数字太小了!请重新输入!!!")
    else:
        print("恭喜你!猜对啦!!!")
        break
print("随机生成的数字是:",random_num)
"""
# 练习1:将1-1000之间(含1000)所有的5的倍数的数字累加起来
# toatl = 0
# for i in range(1001):
#     if i % 5 == 0:
#         toatl += i
# print(f"和为:{toatl}")


# 练习2:统计字符串
# "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# 中有多少个a和k

s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
count_a = 0
count_k = 0
for c in s:
    if c == "a":
        count_a += 1
    elif c == "k":
        count_k += 1
print(f"a的个数为:{count_a}")
print(f"k的个数为:{count_k}")


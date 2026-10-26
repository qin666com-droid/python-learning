"""
案例:
1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积= 底*高/2)。
2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)
3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、
最低分、平均分(保留1位小数)，并返回。
"""
#案例1:
# def triangle_area(a,h):
#     """
#     计算三角形面积
#     :param a: 三角形的底
#     :param h: 三角形的高
#     :return: 三角形的面积
#     """
#     return a*h/2
# print("底为3,高为4的三角形面积为:",triangle_area(3,4))
#
# #案例2:
# def count_aeiou(s):
#     num = 0
#     for c in s:
#         if c in 'aeiouAEIOU':
#             num = num + 1
#     return num
# print(count_aeiou("fsjinsioodsna"))
#
# # 案例3:
# def student(score_list):
#     max_score = max(score_list)
#     min_score = min(score_list)
#     avg_score = round(sum(score_list)/len(score_list),1)
#     return max_score, min_score, avg_score
# max_score, min_score, avg_score = student([456,789,553,786,123,254])
# print(f"最高分:{max_score},最低分:{min_score},平均分:{avg_score}")


#练习:
#1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数>=90:A
# 分数>= 75:B
# 分数>=60:C
# 分数〈60:D
# def grade(score):
#     """
#     根据传入的分数，计算对应的分数等级并返回。
#     :param score: 输入的分数
#     :return: 对应的等级
#     """
#     if score >= 90:
#         return 'A'
#     elif score >= 75:
#         return 'B'
#     elif score >= 60:
#         return 'C'
#     else:
#         return 'D'
#
# print(grade(90))
# print(grade(80))
# print(grade(70))
# print(grade(50))
#2.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
#字符串反转，如果和原字符串相同，就是回文串。
#如:"level"，"radar"，"黄山落叶松叶落山黄")
# def hui(s_list):
#     """
#     判断是否是回文串
#     :param s_list:输入活传入字符串
#     :return: 返回结果:是/否
#     """
#     if s_list == s_list[::-1]:
#         return True
#     else:
#         return False
# print(hui("lalal"))

#3.定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def time(seconds):
#     hours = seconds // 3600
#     re_seconds = seconds % 3600
#     minutes = re_seconds // 60
#     sec = re_seconds % 60
#     return hours, minutes, sec
# h,m,s =time(60000)
# print(f"小时:{h},分钟:{m},秒:{s}")

#4.定义一个函数:根据传入的三角形三个边的边长，
# 判定三角形的类型(等边、等腰、普通，或者不能构成三角形)。
def sjx(a,b,c):

    if a+b>c and a+c>b and b+c>a:
        if a == b == c:
            return "能构成三角形并且是等边三角形!"
        elif a == b or c == b or c == a:
            return "能构成三角形并且是等腰三角形!"
        else:
            return "能构成三角形并且是普通三角形!"
    else:
        return "不能构成三角形!"
    # return
print(sjx(6,5,1))





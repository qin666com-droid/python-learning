#match...case 模式匹配: 工作日程安排
# day = input("请输入星期几:")
# match day:
#     case "1":
#         print("周一:工作日")
#     case "2":
#         print("周二:学习日")
#     case "3":
#         print("周三:吃喝日")
#     case "4":
#         print("周四:玩乐日")
#     case "5":
#         print("周五:锻炼日")
#     case "6"|"7":
#         print("周末:吃喝玩乐日")
#     case _:
#         print("输入错误!!")


# 案例: 基于match...case 实现简易计算器
#实现+ - * / 运算
# num1 = float(input("请输入第一个数:"))
# num2 = float(input("请输入第二个数:"))
# op = input("请输入运算符(+,-,*,/):")
# match op:
#      case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#      case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#      case "*":
#          print(f"{num1} * {num2} = {num1 * num2}")
#      case "/" if num2!=0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#      case _:
#          print("操作不支持")

# 案例:输入指令,实现动作
mas = input("请输入指令:")
match mas:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"| " " :
        print("角色跳跃")
    case "攻击"|"j"|"J":
        print("角色发动攻击")
    case "退出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("操作不支持!")


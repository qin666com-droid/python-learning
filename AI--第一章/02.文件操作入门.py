#读文件
# #1.打开文件
# f = open("./recources/咯咯咯咯咯.txt", "r", encoding="utf-8")
#
#
# #2.读取文件内容
# # content = f.read()
# # print(content)
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip())
#
# #3.关闭文件
# f.close()



# #写文件
# #1.打开文件
# f = open("./recources/静夜思.txt", "w", encoding="utf-8")
#
#
# #2.写入文件内容
# f.write("静夜思\n\n")
# f.write("床前明月光,疑是地上霜。\n")
# f.write("举头望明月,低头思故乡。")
#
# #3.关闭文件
# f.close()


#----------------------------释放资源--方式一-----------
# #写文件
# #1.打开文件
# f = open("./recources/静夜思.txt", "w", encoding="utf-8")
#
# try:
#     #2.写入文件内容
#     f.write("静夜思\n\n")
#     f.write("床前明月光,疑是地上霜。\n")
#     f.write("举头望明月,低头思故乡。")
#
# finally:
#     #3.关闭文件
#     f.close()

#----------------------------释放资源--方式二(最佳实践)-----------
#写文件
#1.打开文件
with open("./recources/静夜思.txt", "w", encoding="utf-8") as f:
    #2.写入文件内容
    f.write("静夜思\n\n")
    f.write("床前明月光,疑是地上霜。\n")
    f.write("举头望明月,低头思故乡。")








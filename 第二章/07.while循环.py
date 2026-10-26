# while 循环 (关注的是循环的条件)
# i =0
# while i<10:
#     print("人生苦短")
#     i+=1
# else:
#     print("over")

# while 案例: 计算1-100间所有偶数的累加之和
total = 0
i =1
while i<=100:
    if i%2==0:
        total+=i
    i +=1
print(f"和为:{total}")




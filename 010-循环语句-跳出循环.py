# 跳出循环
# break
list1 = [22, 33, 44, 0, -11, -3, 93, 69, 77]
flag = False
number = 1
for i in list1:
    if i < 0:
        flag = True
        break
    print("已经执行了 {} 次".format(number))
    number += 1

if flag:
    print("列表中有负数")
else:
    print("列表中没有负数")

# continue 退出本次循环，下一次继续
list2 = [22, 33, 44, 0, -11, -3, 93, 69, 77]
for j in list2:
    if j < 0:
        continue
    print(j)


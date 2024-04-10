# 使用while循环计算1~100内所有奇数之和
i = 1
total = 0
while i <= 100:
    if i % 2 == 1:
        total += i
    i += 1
print("1~100所有奇数之和:", total)

# 计算一个列表中的奇数和偶数的个数
list1 = [11, 24, 22, 28, 99, 39, 69, 55, 33, 44, 13, 14]
j = 1
odd_num = 0
even_num = 0
while j < len(list1):
    if list1[j] % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    j += 1
print("奇数个数:", odd_num)
print("偶数个数:", even_num)




# # 循环语句-while
# # 增值
# i = 0
# while i < 10:
#     # print(i)
#     i += 1
#
# a = 5
# while a > 0:
#     # print(a)
#     a -= 1
#
# # 输出偶数
# x = 2
# while x < 10:
#     # print(x)
#     x += 2
#
# # 输出奇数
# y = 1
# while y < 10:
#     # print(y)
#     y += 2
#
# a = 1
# while a < 10:
#     # if a % 2 == 1:
#         # print(a)
#     a += 1
#
# username = input("请输入用户名: ")
# while not username:
#     username = input("请输入用户名: ")
# print("hello,", username)

# 遍历列表
# list1 = ['乾', '坤', '震', '巽', '坎', '离', '艮', '兑']
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

# 案例：提取列表中的偶数和奇数
list1 = [39, 22, 13, 14, 99, 88, 56, 23, 18, 19]
i = 0
odd_list = []
even_list = []
while i < len(list1):
    if list1[i] % 2 == 0:
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
    i += 1
print("奇数列表", odd_list)
print("偶数列表", even_list)


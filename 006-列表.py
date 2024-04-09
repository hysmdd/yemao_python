
list1 = ['乾', '坤', '震', '巽', '坎', '离', '艮', '兑']

# print(list1[4], list1[-4])
# print(list1[-1])
# print(list1[1:6])   # 左闭右开
# print(list1[1:])
# print(list1[:6])
# print(list1[1:8:2])  # start:end:step

list2 = [11, 55, 33, 99, 22]
print("长度", len(list2))
print("最大值", max(list2))
print("最小值", min(list2))
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# 添加元素
list2.append(44)
list2.append(20.34)
print(list2)

# 删除元素
del list2[0]
print(list2)

# 修改元素
list2[0] = 99
print(list2)

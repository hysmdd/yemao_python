# 创建一个10个元素的列表
# 提取后5个元素的值
# 在列表末尾中添加一个元素666
# 删除列表的第一个元素

list1 = [13, 14, 20, 33, 66, 22, 11, 88, 99, 77]
print("后五个元素的值", list1[-5::1])
list1.append(666)
print("末尾追加元素666", list1)
del list1[0]
print("删除列表第一个元素", list1)

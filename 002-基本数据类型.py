# 基本数据类型
# a = 2
# print(type(a))  # int
# b = 3.14
# print(type(b))  # float
# c = "Hello World"
# print(type(c))  # str
# d = int(b)
# print(type(d))  # int
# e = float(a)
# print(type(e), e)   # float
# f = str(a)
# print(type(f), f)   # str
# 不能计算
# g = 2 + f
# print(type(g))
# g = 2 + int(f)
# print(g)
# f = False
# print(type(f))  # bool

data = ['三尸语', 3.14, 339, True]
print(data[0])  # 三尸语
print(data[-2]) # 339

temp = [23, 25, 25, 28, 30, 28, 28]
print("周一的温度是：", temp[0], "度")
print("周一的温度是" + str(temp[0]) + "度")
print(f"周一的温度是{temp[0]}度")

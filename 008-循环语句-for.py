# for循环

# 遍历列表
list1 = ['乾', '坤', '震', '巽', '坎', '离', '艮', '兑']
for item in list1:
    print(item)

# 遍历元祖
tuple1 = ('乾', '坤', '震', '巽', '坎', '离', '艮', '兑')
for item in tuple1:
    print(item)

# 遍历字符串
c = 'Coderqin'
for item in c:
    print(item)

# 遍历字典
profile = {
    'username': 'dex',
    'age': '18',
    'gender': 'female',
}
# 取键值对
for key, value in profile.items():
    print(key, value)
# 取键
for key in profile.keys():
    print(key)
# 取值
for value in profile.values():
    print(value)

# range
a = range(10)
print(a)
b = list(a)
print(b)

for i in range(10):
    print(i)

# 案例：计算1-100的和
total = 0
for i in range(1, 101):
    total += i
print("sum = {}".format(total))

tt = sum(range(1, 101))
print(tt)

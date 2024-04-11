# 判断一个人名是否在列表中-使用break语句
names = ['洛小阳', '凌绛', '张破虏', '洛朝廷', '吴听寒', '陈寺青', '彭瑊', '陈恩义']
flag = False
for name in names:
    if name == '彭瑊':
        flag = True
        break
print("彭瑊是否在列表中:", flag)

# 打印出列表中所有大于100的数字-使用continue语句
nums = [0, 3, 2, 101, -10, 999, 78, 187]
for num in nums:
    if num < 100:
        continue
    print(num)


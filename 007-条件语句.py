# 条件语句
# 比较运算符：>  >=  <  <=  !=  ==

# 单一判断
if 3 > 2:
    print('3 > 2')

# 二选一
a = 3
b = 9
if a > b:
    number = a
else:
    number = b
print("最大值是 {}".format(number))

# 多选一
# 优秀（>90），良好（80-90），及格（60-80），不及格（0-60）
score = 39
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


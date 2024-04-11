# 函数

# 自定义函数
# 案例：根据半径计算圆的半径
# 无参无返回值
def area1():
    print(3.14 * 5 * 5)


# 有参无返回值
def area2(r):
    print(3.14 * r * r)


# 无参有返回值
def area3():
    return 3.14 * 5 * 5


# 有参有返回值
def area4(r):
    return 3.14 * r * r


area1()
area2(5)
print(area3())
a = area4(5)
print(a)


# 作用域
msg = "全局变量"


def speak():
    global msg
    msg = "局部变量"
    print(msg)


print(msg)
speak()
print(msg)

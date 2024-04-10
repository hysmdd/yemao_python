# 使用for循环计算1~100内所有奇数和偶数之和

odd_total = 0
even_total = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i
print("1~100奇数之和: {}".format(odd_total))
print("1~100偶数之和: {}".format(even_total))


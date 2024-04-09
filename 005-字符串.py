# 字符串

# temp = 23
# station = "大雾"
# s1 = "今天的天气是: " + str(temp) + " ℃"
# s2 = "今天的天气是: {} ℃，天气状况：{}".format(str(temp), station)
# s3 = f"今天的天气是: {temp} ℃，天气状况：{station}"
# print(s1)
# print(s2)
# print(s3)

# city = 'chongqing'
# url = 'https://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=83b30d525bff7db3e396e99abc62bd75'.format(city)
# print(url)

s4 = "Python爬虫工程师"
# print(s4[0])
# print(s4[-1])
# print(s4[0:6])  # 左闭右开
# print(s4[6:8])
# print(s4[8:])
# print(s4[:6])
# print(s4.index('爬虫'))
# print(s4.index('abc'))

email_addr = '12345@qq.com'
# print(email_addr.endswith('qq1.com'))   # False
print(email_addr.endswith('qq.com'))    # True
print(email_addr.startswith('123'))     # True

# len获取字符串的长度
print(len(email_addr))

# 字符串和列表互相转换
email_addr_list = list(email_addr)
print(email_addr_list)
print("".join(email_addr_list))

# 从终端获取字符串
s5 = input("请输入：")
print(f"您输入的字符串是：{s5}")

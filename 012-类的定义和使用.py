# 类的定义和使用
class People:
    # 初始化
    def __init__(self, name, age, sex):
        print("开始初始化")
        self.name = name
        self.age = age
        self.sex = sex
        print("结束初始化")

    def speak(self):
        print(f"{self.name}正在说话...")


lingjiang = People("凌绛", 18, "女")
print(f"姓名：{lingjiang.name}")
print(f"年龄：{lingjiang.age}")
print(f"性别：{lingjiang.sex}")
lingjiang.speak()

luoxiaoyang = People("洛小阳", 18, "男")
luoxiaoyang.age = 19
print(luoxiaoyang.age)
luoxiaoyang.height = 179
print(luoxiaoyang.height)
del luoxiaoyang.sex

zhangpolu = People("张破虏", 24, "男")
wutinghan = People("吴听寒", 23, "女")
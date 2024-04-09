# 根据不同的年龄判断所处的阶段
# 小于18岁，青少年儿童
# 18~60岁，成年
# 大于60岁，老年人

age = int(input("请输入年龄："))
if age < 18:
    print("青少年儿童")
elif age <= 60:
    print("成年")
else:
    print("老年人")

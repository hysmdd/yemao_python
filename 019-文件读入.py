# 文件读入

# f = open(r'D:\data\python\夜猫编程\file\test1.txt', mode='r', encoding='utf-8')

# txt = f.read()
# txt = f.readline()
#
# print(txt)

# txt = f.readline()
# print(txt, end='')
# while txt:
#     txt = f.readline()
#     print(txt, end='')

# txt = f.readlines()
# print(txt)
#
# f.close()
# print(f.closed)


with open(r'D:\data\python\夜猫编程\file\test1.txt', mode='r', encoding='utf-8') as f:
    txt = f.read()
    print(txt)

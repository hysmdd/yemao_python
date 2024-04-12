# 文件操作-文件写入

s = '三尸语'

li = ['三尸语', '三尸语番外篇', '阴阳诡匠']

# with open(r'D:\data\python\夜猫编程\file\test3.txt', mode='w', encoding='utf-8') as f:
#     # f.write(s)
#     f.writelines(li)

# 复制文件
# f1 = open('./file/test1.txt', mode='r', encoding='utf-8')
# f2 = open('./file/test2.txt', mode='w', encoding='utf-8')
# f2.writelines(f1.readlines())
# f1.close()
# f2.close()

with open(r'D:\data\python\夜猫编程\file\test3.txt', mode='a', encoding='utf-8') as f:
    # f.write(s)
    f.writelines('三尸语3')

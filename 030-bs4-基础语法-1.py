# BeautifulSoup4基础语法
from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>Lighter And Princess</title>
    </head>
    <body>
        <p class="title" name="lixun"></p>
        <p class="story">You can make money without doing evil.
    <a href="https://www.imqinhao.cn/lixun" class="sister" id="link1">Zhuyun</a>
    <a href="https://www.imqinhao.cn/zhuyun" class="sister" id="link2"><!-- Lixun --></a> and
    <a href="https://www.imqinhao.cn/rendi" class="sister" id="link3">Rendi</a>
    are good friends.</p>
    <b><!-- You can make money without doing evil. --></b>
'''

soup = BeautifulSoup(html, 'html.parser')
# 获取标签
print(soup.a)
print(type(soup.a))
# 获取标签的名称
print(soup.a.name)
# 获取标签的属性名
print(soup.a.attrs)
print(soup.a['href'])
print(soup.a.get('id'))
# 改变标签的属性值
soup.a['class'] = 'brother'
print(soup.a)
# 获取标签的文本内容
print(soup.a.string)
print(soup.a.text)
print(soup.a.get_text())
print(type(soup.a.string))
# 获取注释部分文本内容
from bs4.element import Comment
print(soup.b.string)
print(type(soup.b.string))
# 遍历文档树
body_tag = soup.body
# 返回所有的子节点
print(body_tag.contents)
# 返回所有子节点的迭代器
for tag in body_tag.children:
    print(repr(tag))
# 返回所有文本内容
for tag in body_tag.strings:
    print(repr(tag))
# 使用 stripped_strings可以去除多余空白内容
for tag in body_tag.stripped_strings:
    print(tag)


# xPath lxml库使用
from lxml import etree

# 读取本地的xml html文件
# xml = etree.parse('./file/hello.xml')
# print(etree.tostring(xml).decode())

with open('./file/test1.html', 'r', encoding='utf-8') as f:
    text = f.read()
html = etree.HTML(text)
# 子节点和子孙节点的定位
result = html.xpath('/html/head/title/text()')
result1 = html.xpath('//head/title/text()')
result2 = html.xpath('//title/text()')
print(result, result1, result2)

# 通过属性值定义标签
# result3 = html.xpath('//div[@class="actor"]')
# print(result3)
result4 = html.xpath('//div[@class="actor"]/a[@target="_self"]/text()')
print(result4)
result5 = html.xpath('//div[@class="actor"]/a[@class]/text()')
print(result5)

# 按照顺序来定位标签
result6 = html.xpath('//div[@class="actor"]/p[1]/text()')
result7 = html.xpath('//div[@class="actor"]/p[last() - 2]/text()')
print(result6, result7)

# 按照所包含的元素来定位
result8 = html.xpath('//div[p and a]//text()')
print(result8)

# 在对象中继续取值
result9 = html.xpath('//div[@class="actor"]')[0]
name = result9.xpath('./a[1]/@href')[0]
print(name)

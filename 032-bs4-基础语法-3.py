from bs4 import BeautifulSoup

html = '''
<table class="grid" width="100%" align="center">
<caption>搜索结果</caption>
    <tr align="center" style="height: 30px;">
        <th width="20%">文章名称</th>
        <th width="40%">最新章节</th>
        <th width="15%">作者</th>
        <th width="9%">字数</th>
        <th width="6%">状态</th>
    </tr>
    <tr id="nr">
        <td class="odd"><a href="/16_10086">打火机与公主裙·荒草园</a></td>
        <td class="even"><a href="/16_10086/6546451.html" target="_blank">第59章</a></td>
        <td class="odd">Twentine</td>
        <td class="even">2476K</td>
        <td class="odd" align="center">2016-04-24</td>
        <td class="even" id="center" align="center">完结</td>
    </tr>
    <tr id="nr">
        <td class="odd"><a href="/16_10123">打火机与公主裙·长明灯</a></td>
        <td class="even"><a href="/16_10123/154456.html" target="_blank">第55章 走马灯</a></td>
        <td class="odd">Twentine</td>
        <td class="even">1234K</td>
        <td class="odd" align="center">2016-10-16</td>
        <td class="even" align="center">完结</td>
    </tr>
    <tr id="nr">
        <td class="odd"><a href="/19_10526">三尸语</a></td>
        <td class="even"><a href="/19_10526/413252022.html" target="_blank">第419章 万事不全</a></td>
        <td class="odd">洛小阳</td>
        <td class="even">1111K</td>
        <td class="odd" align="center">2019-01-23</td>
        <td class="even" align="center">完结</td>
    </tr>
    <tr id="nr">
        <td class="odd"><a href="/21_13025">阴阳诡匠</a></td>
        <td class="even"><a href="/21_13025/251546546.html" target="_blank">第379章 再也不分开</a></td>
        <td class="odd">洛小阳</td>
        <td class="even">1058K</td>
        <td class="odd" align="center">2021-12-17</td>
        <td class="even" align="center">完结</td>
    </tr>
    <tr id="nr">
        <td class="odd"><a href="/10_10770">她死在QQ上</a></td>
        <td class="even"><a href="/10_10770/41306831.html" target="_blank">第11章 尾声</a></td>
        <td class="odd">马伯庸</td>
        <td class="even">268K</td>
        <td class="odd" align="center">2006-01-23</td>
        <td class="even" align="center">完结</td>
    </tr>
    <p>
        <a id="link1">Test</a>
        <c><b id="link2">Test</b></c>
    </p>
</table>
'''

soup = BeautifulSoup(html, "html.parser")

# 1. 查找所有 tr 标签
# print(soup.select('tr'))

# 2. 查找所有类名是 odd 的标签
# print(soup.select('.odd'))

# 3. 查找所有 id 是 center 的标签
# print(soup.select('#center'))

# 4. 组合查找
# p标签下，包含属性值为 id=link2的标签
# print(soup.select('p #link2'))

# 5. p标签下，所有的a标签
# print(soup.select('p a'))

# 6. 查找属性值为 target="_blank"的 a标签
# print(soup.select("a[target='_blank']"))

# 7. 获取属性值及文本
# 获取a标签的文本内容，及href的属性值
a = soup.select('a')
for i in a:
    print(i.text)
    print(i.get('href'))


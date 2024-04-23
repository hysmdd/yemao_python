# bs4 find()和 find_all()方法
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
        <td class="even" align="center">完结</td>
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
</table>
'''

soup = BeautifulSoup(html, "html.parser")

# 1. 获取第一个tr标签
# tr = soup.find('tr')
# print(tr)

# 2. 获取所有的tr标签
# trs = soup.find_all('tr')
# print(trs)
# for tr in trs:
#     print(tr)
#     print('=' * 30)

# 3. 获取所有id = nr的tr标签
# trs = soup.find_all('tr', id = 'nr')
# for tr in trs:
#     print(tr)
#     print("=" * 30)
# trs = soup.find_all('tr', attrs={'id': 'nr'})
# for tr in trs:
#     print(tr)
#     print("=" * 30)

# 4. 将所有class等于odd，align等于center的td标签提取出来
# tds = soup.find_all("td", class_="odd", align="center")
# tds = soup.find_all("td", attrs={'class': 'odd', 'align': 'center'})
# for td in tds:
#     print(td)
#     print("=" * 30)

# 5. 获取所有属性target="_blank" a标签的href属性
# a_list = soup.find_all("a", target="_blank")
# for a in a_list:
#     print(a['href'])
#     print("*" * 30)

# 6. 获取所有小说名称，链接，以及作者和日期信息，用列表的方式打印出来
trs = soup.find_all('tr', attrs={'id': 'nr'})
info = []
for tr in trs:
    tds = tr.find_all('td')
    link = tds[0].a['href']
    name = tds[0].a.string
    author = tds[2].string
    date = tds[4].text
    info.append([name, link, author, date])
print(info)

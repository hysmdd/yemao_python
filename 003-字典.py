# 字典
role = {
    'name': '凌降',
    'gender': 'female'
}
print(role['name'])
print(role['gender'])

singer = {
    "name": '邓紫棋',
    "songs": ["来自天堂的魔鬼", "A.I.N.I.", "Where did U go", "泡沫", "喜欢你"]
}
print(singer['songs'][3])
singer['songs'][0] = "倒数"
singer['gender'] = 'female'
print(singer)

# 案例：天气预报
weather = {
    "temp": [23, 24, 23, 25, 26, 26, 30],
    "station": ["晴", "小雨", "大雨", "中雨", "多云", "阴", "阵雨", "大雪", "冰雹", "雾霾", "晴转多云"]
}
print(f"周一的温度是：{weather['temp'][0]}度，天气状况：{weather['station'][5]}")

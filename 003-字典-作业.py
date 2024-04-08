weather = {
    "temp": [25, 25, 26, 28, 26, 24, 25],
    "station": ["晴", "小雨", "大雨", "中雨", "多云", "阴", "阵雨", "大雪", "冰雹", "雾霾", "晴转多云"],
    "city": ["深圳", "重庆", "上海", "武汉", "厦门", "长沙", "广州"]
}

print(f"{weather['city'][1]}周一的天气{weather['station'][-1]}，温度是{weather['temp'][4]}摄氏度")
print(f"{weather['city'][-2]}周三的天气{weather['station'][5]}，温度是{weather['temp'][2]}摄氏度")

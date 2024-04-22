# 转义字符和原生字符串
import re

# Python转义字符
# raw 原生
text = r"Hello\World\\npython"
print(text)

# 正则表达式中的转移字符
text1 = "The subscription fee is $99 and tax is $15"
result = re.findall('\$\d+', text1)
print(result)

text2 = "abc888\water"
result = re.findall("(\d+)\\\\", text2)
result2 = re.findall(r"(\d+)\\", text2)
print(result)
print(result2)

text3 = "<title >华为Pura70 Ultra首销沉浸式开箱 - AcFun弹幕视频网 - 认真你就输啦 (?ω?)ノ- ( ゜- ゜)つロ</title>"
result = re.findall(r"<title >(.*?) - AcFun弹幕视频网 - 认真你就输啦 \(\?ω\?\)ノ- \( ゜- ゜\)つロ</title>", text3)
print(result[0])

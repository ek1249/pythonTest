import requests
import re

url = "http://211.251.214.169:8080/SeatMate_sj/SeatMate.php?classInfo=1"
str = requests.get(url)
print(str)
print(str.text)
text = bytes(str.text,"iso-8859-1").decode("euc-kr");
#print(text)
#빈좌석을 모두 출력해봅시다.
title = re.findall("<title>(.*)</title>",text)
print(title)
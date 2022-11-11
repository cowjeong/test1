import requests
from bs4 import BeautifulSoup
import math

header = {'User-agent' : "Mozila/2.0"}
response = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8', headers = header)
html = response.text
soup = BeautifulSoup(html,"html.parser")
title = soup.select_one('.temperature_text')

ondo_full = title.text.strip()
ondo_num1 =ondo_full[5:10]
ondo_num = math.ceil(float(ondo_full[5:9]))

print("[[현재 성결의 날씨]]")
print(ondo_num1)
print(math.ceil(ondo_num), type(ondo_num))


if ondo_num >= 28:
    print("민소매, 반팔, 반바지, 짦은 치마, 린넨 옷")
elif (ondo_num <= 27 and ondo_num >= 23):
    print("반팔, 얇은 셔츠, 반바지, 면바지")
elif (ondo_num <=22 and ondo_num >= 20):
    print("블라우스, 긴팔 티, 면바지, 슬랙스")
elif (ondo_num <= 19 and ondo_num >= 17):
    print("얇은 가디건이나 니트, 맨투맨, 후드, 긴 바지")
elif (ondo_num <= 16 and ondo_num >= 12):
    print("자켓, 가디건, 청자켓, 니트, 스타킹, 청바지")
elif (ondo_num <= 11 and ondo_num >= 9):
    print("트렌치코트, 야상, 점퍼, 스타킹, 기모바지")
elif (ondo_num <= 8 and ondo_num >= 5):
    print("울 코트, 히트텍, 가죽 옷, 기모")
else:
    print("패딩, 두꺼운 코트, 누빔 옷, 기모, 목도리 ")


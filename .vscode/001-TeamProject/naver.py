import requests
from bs4 import BeautifulSoup


header = {'User-agent' : 'Mozila/2.0'}
response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.cluster_text_headline')
print(title)
#print(weathers.text.strip())



'''28도 민소매티, 반팔, 반바지
23~27도 반팔, 얇은 셔츠, 반바지
20~22도 긴팔티, 얇은 가디건, 면바지
17도~19도 얇은 니트, 후드, 맨투맨
12~16도 얇은 재킷, 니트, 청바지
9~11도 재킷, 트렌치 코트, 니트
5~8도 코트, 니트, 두꺼운 바지
4도~ 롱패딩, 두꺼운 코트, 기모제품'''

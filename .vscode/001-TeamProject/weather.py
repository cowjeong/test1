import requests
from bs4 import BeautifulSoup

url ="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8&tqi=h2Kc7dprvOsssbyKTbsssssssIZ-258995"
header = {'User-agent' : 'Mozila/2.0'}
response = requests.get( url , headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

weathers = soup.select_one('.status_wrap')
for weather in weathers:
    print(weather.text.strip())
    
print('오늘의 날씨')
current_temperature = soup.select_one('.temperature_text')
print(current_temperature.text.strip())
print('오늘의 날씨')
weathers1 = soup.select_one('.weather_graphic')
print(weathers1.text.strip()) 
print('\n')


print(' 기온별 옷차림 추천 ')
print(' 28°    민소매티, 반팔, 반바지\n',
'23~27° 반팔, 얇은 셔츠, 반바지\n',
'20~22° 긴팔티, 얇은 가디건, 면바지\n',
'17~19° 얇은 니트, 후드, 맨투맨\n',
'12~16° 얇은 재킷, 니트, 청바지\n',
'9~11°  재킷, 트렌치 코트, 니트\n',
'5~8°   코트, 니트, 두꺼운 바지\n',
'4°~    롱패딩, 두꺼운 코트, 기모제품\n')



   
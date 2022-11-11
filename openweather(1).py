# 날씨 API (Application Programing Interface)
import requests
api_endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
api_key = 'c691578d0e8c24c881f2c801e66c3e58'

weather_params = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": api_key
}
response = requests.get(api_endpoint, params=weather_params)
print(response.status_code)
  
'''so .. why this program doesn't work ??????
I don't know why .....
This is my school assignment ....
In addition, the deadline for this assignment is two weeks away .. 
You know what I'm saying ??????????????????????????     
YOU got it ????
FUCK UP ,,,,,,,,,,,,,,,'''


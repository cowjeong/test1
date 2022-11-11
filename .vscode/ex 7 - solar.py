seoul_sun = 1865
jeju_sun = 1767
busan_sun = 2167
genel = 15
seoul_energy = seoul_sun * genel
jeju_energy = jeju_sun * genel
busan_energy = busan_sun * genel
print(f"서울의 일조시간: {seoul_sun} hours")
print(f"서울의 발전량: {seoul_energy} wh\n")
print(f"제주의 일조시간: {jeju_sun} hours")
print(f"제주의 발전량: {jeju_energy} wh\n")
print(f"부산의 일조시간: {busan_sun} hours")
print(f"부산의 발전량: {busan_energy} wh\n")

incheon_sun = 2171
gwangju_sun = 2005

incheon_energy = incheon_sun * genel
gwangju_energy = gwangju_sun * genel

print(f"인천의 일조시간: {incheon_sun} hours")
print(f"인천의 발전량: {incheon_energy} wh\n")
print(f"광주의 일조시간: {gwangju_sun} hours")
print(f"광주의 발전량: {gwangju_energy} wh\n")

# 객체지향 프로그래밍으로 
genel = 15 
class Solar():
    def __init__(self, city, sunny):
        self.sunny = sunny
        self.city = city

    def print_city(self):
        print(f"{self.city}의 일조시간: {self.sunny} hours")
        output = self.sunny * genel / 1000
        print(f"{self.city}의 발전량: {output} kwh\n")

seoul_energy = Solar("서울", 1865)
jeju_energy = Solar("제주", 1767)
busan_energy = Solar("부산", 2167)
incheon_energy = Solar("인천", 2171)
gwangju_energy = Solar("광주", 2005)

seoul_energy.print_city()
jeju_energy.print_city()
busan_energy.print_city()
incheon_energy.print_city()
gwangju_energy.print_city()
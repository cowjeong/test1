import math

a = math.pow(2, 3)
b = math.sqrt(4)

print('math.pow(2, 3)=', a)
print('math.sqrt(4)=', b)
del math   #math 해제, 삭제되면 정의되지 않아서 오류 발생
import importlib 
import math
importlib.reload(math)
print(dir(math))
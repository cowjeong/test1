def f_a():
    num = 20
    print("f_a()의 num값 %d" % num)

def f_b():
    print("f_b()의 num값 %d" % num)

num = 10
f_a() #지역변수 20 출력
f_b() #전역변수 10 출력
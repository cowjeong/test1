def f_a():
    global num
    num = 20
    print("f_a()의 num값 %d" % num)

num = 10
f_a()
print("전역변수 num값 %d" % num)
class UnderSelf:
    def meth1(self):
        print("python 1")
    def meth2():
        print("python 2")

s1 = UnderSelf()
s1.meth1()
print('id(s1)=', id(s1))
print('id(s1.meth1()=', id(s1.meth1()))

#동일한 인스턴스 s1을 호출한 것이므로 메모리 주소도 같음
UnderSelf.meth2()
print('id(UnderSelf.meth2()=', id(UnderSelf.meth2())) 
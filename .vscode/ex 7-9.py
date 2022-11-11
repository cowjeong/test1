class UnderSelf:
    def meth1(self):
        print("python 1")
    def meth2(self):
        print("python 2")

s1 = UnderSelf()
s2 = UnderSelf()
s1.meth1()
print('id(s1) = ', id(s1))
s2.meth2()
print('id(s2)=', id(s2))
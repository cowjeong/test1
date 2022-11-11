class UnderSelf:
    def meth1(self):
        print("python 1")
    def meth2():
        print("python 2")

s1 = UnderSelf()
s1.meth1()
print('id(s1)=', id(s1))
print('id(s1.meth1()=', id(s1.meth1()))

UnderSelf.meth2()
print('id(UnderSelf.meth2()=', id(UnderSelf.meth2())) 

UnderSelf.meth1(s1)
print('id(UnderSelf.meth1(s1))=', id(UnderSelf.meth1(s1))) 
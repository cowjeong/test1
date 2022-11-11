class UnderSelf:
    def meth1(self):
        print("python 1")
    def meth2(self):
        print("python 2")

s1 = UnderSelf()
s1.meth1()
print('id(s1)=', id(s1))
print('id(s1.meth1())=', id(s1.meth1()))
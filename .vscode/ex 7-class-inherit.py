class Calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

Calc1 = Calc(4, 2)              #cacl 객체 생성 
print('calc1.add()= ', Calc1.add())
print('calc1.div()= ', Calc1.div())

class InheritCalc(Calc):          #InheritCalc 클래스는 calc 클래스를 상속받음
    pass
    
Calc2 = InheritCalc(6,2)
print('Calc2.add()= ', Calc2.add())
print('Calc2.mul()=', Calc2.mul())
print('Calc2.sub()=', Calc2.sub())
print('Calc2.div()=', Calc2.div())

class InheritCalc(Calc):            #InheriCalc 클래스에 trpl() 메소드 추가하여 클래스 기능 확장
    def power(self):
        result = self.first ** self.second
        return result

    
Calc3 = InheritCalc(4,2)
print('Calc3.power()=',Calc3.power())

#d = Calc(4,0)
#print(d.div())

#메소드오버라이딩(Method Overriding)
#클래스 Calc를 상속받아 매소드 오버라이딩하는 클래스 SafeDivCalc
class SafeDivCalc(Calc):      
    def div(self):
        if self.second == 0 :   #나누는 값이 0인 경우 리턴하도록 수정
            return 0
        else :
            return self.first / self.second

Calc4 = SafeDivCalc(4,0)
print('Calc4.div()=', Calc4.div())
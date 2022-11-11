def calc(v1, v2, op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == ' / ' :
        if var2 == 0 :
            return 'error'
        else :
            result = v1 / v2
    elif op == '**' :
        result = v1 ** v2
    return result 

res, var1, var2, opper = 0, 0, 0,  ''

while True : 
    oper = input("연산자를 입력하세요(+, -, *, /, **, 종료: q)")
    if oper == 'q' :
        print("프로그램을 종료합니다.")
        break
    var1 = int(input("첫 번쨰 수를 입력하세요: "))
    var2 = int(input("두 번째 수를 입력하세요: "))
    res = calc(var1, var2, oper)
    if res == 'error' :
        print("0으로 나누면 안됩니다.")
    else :
        print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))
        
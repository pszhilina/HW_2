from operator import mul
t=float(input("Длительность разговора: "))
code = int(input("Код города: "))
def f(t,code):
    if code==343:
        return mul(t,15)
    elif code==381:
        return mul(t,18)
    elif code==473:
        return mul(t,13)
    elif code==485:
        return mul(t,11)
    else:
        return("Неизвестный код")
print(f(t,code))

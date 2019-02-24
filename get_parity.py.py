#get parity
x=int(input("Введите целое число: "))
def f(x):
    return x%2
if f(x)==0:
    print("Чётное")
else:
    print("Нечётное")

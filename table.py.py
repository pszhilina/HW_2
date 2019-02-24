# Homework 2.1
value = int(input("Введите номер элемента: "))
if value:
    num=int(value)
    if num==3:
        print("Литий")
    elif num==25:
        print("Марганец")
    elif num==80:
        print("Ртуть")
    elif num==17:
        print("Хлор")
    else:
        print("Что это?")
else:
    print("Попробуйте еще раз")
    

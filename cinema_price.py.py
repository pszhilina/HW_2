from operator import mul
print("Программа для подсчета стоимости билетов в кино")
film=str(input("Выберите фильм: "))
date=str(input("Сегодня или завтра? "))
time=float(input("Выберете время: "))
num=float(input("Введите количесво билетов: "))
print("Вы выбрали фильм: ", film, ", день: ", date, ", количество билетов: ", num)
def sale(num,date):
    if num>=20:
        if date=="завтра":
            return sum(0.2, 0.05)
        else:
            return 0.2
    else:
        if date=="завтра":
            return 0.05
        else:
            return 0
def price(film, time):
    if film=="Пятница":
        if time==12:
            return 250
        elif time==16:
            return 350
        elif time==20:
            return 450
        else:
            return 0
    elif film=="Чемпионы":
        if time==10:
            return 250
        elif time==13:
            return 350
        elif time==16:
            return 350
        else:
            return 0
    elif film=="Пернатая банда":
        if time==10:
            return 350
        elif time==14:
            return 450
        elif time==18:
            return 450
        else:
            return 0
    else:
        return 0
if price(film,time)==0:
    print("Ошибка ввода.")
else:
    print("Результат: ", price(film,time)*(1-sale(num,date))*num, " руб.")

        
        

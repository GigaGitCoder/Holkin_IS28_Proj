#V 24
#1. Дано четырехзначное число. Проверить истинность высказывания:
#«Данное число читается одинаково слева направо и справа налево».

while True: #Исключение если пользователь введёт не полное число
    try:
        N=int(input("Введите четырехзначное число для проверки на палиндром: "))
        break
    except:
        print("Вы ввели не численный формат данных.")

print("Число - палиндром" if N == N//1000+N//100%10*10+N//10%10*100+N%10*1000 else "Число - не палиндром")
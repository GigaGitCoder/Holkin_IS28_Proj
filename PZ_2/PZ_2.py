#V 24
#С начала суток прошло N секунд (N - целое). Найти количество
#полных часов, прошедших с начала суток.

while True: #Исключение если пользователь введёт не полное число
    try:
        N=int(input("Введите кол-во секунд прошедших с начала суток: "))
        break
    except:
        print("Вы ввели не численный формат данных.")

print("Кол-во полных минут, прошедших с начала дня: ",  N//3600) #Вывод результата
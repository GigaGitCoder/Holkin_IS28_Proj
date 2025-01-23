# Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Найти количество слов, которые
# содержат ровно три буквы «А»

try:
    input_user = input("Введите строку: ")
    words = input_user.split()
    count = 0

    for word in words:
        if word.lower().count('а') == 3:
            count += 1
            
    print("Количество слов с ровно тремя буквами 'А':", count)

except Exception as e:
    print("Произошла ошибка:", e)

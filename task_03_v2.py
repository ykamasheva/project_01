# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом
month_day = [28,30,31]
user_input = input("Введите номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
if month == 2:
    print('Количество дней во введенном месяце - ',month_day [0])
elif month in (4,6,9,11):
    print('Количество дней во введенном месяце - ',month_day [1])
elif month in (1,3,5,7,8,10,12):
    print('Количество дней во введенном месяце - ',month_day [2])
else:
     print ('Месяц введен некорректно')
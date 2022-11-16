# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

#from pprint import pprint
salary, expenses = 10000, 12000
expenses_1 = 12000
salary_of_year = salary * 12
expenses_lst = []
month = 1
while month <= 11:
      expenses = expenses * 1.03
      expenses_lst.append(expenses)
      month += 1
expenses_of_year = expenses_1 + sum(expenses_lst)
credit = expenses_of_year - salary_of_year
print ('Зарплата за год:', salary_of_year,'рублей','\n', 
       'Расходы за год:', expenses_of_year,'рублей','\n', 
       'Необходимо взять в долг:', credit, 'рублей'
       )      



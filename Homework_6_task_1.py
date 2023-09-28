# Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
#  Функция возвращает истину, если дата может существовать,
# или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
#  Проверку года на високосность вынести в отдельную
# защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на
# проверку.

from datetime import datetime as dt
from sys import argv

x = str(input('Введите дату в формате DD.MM.YYYY:  '))

def checking_date(a):
    try:
        valid_date = dt.strptime(a, '%d.%m.%Y')
    except ValueError:
        return False
    else:
        return True

def _checking_leap(a):
    year_ = int(a.split('.')[2])
    if (year_ % 4 == 0 and year_ % 100 != 0) or year_ % 400 == 0:
        print('Год високосный')
    else:
        print('Год невисокосный')

print(checking_date(x))
if checking_date(x) == True:
    _checking_leap(x)




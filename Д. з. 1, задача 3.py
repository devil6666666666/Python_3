# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint

num = randint(LOWER_LIMIT, UPPER_LIMIT)
i = 0
trying = 10
while i < trying:
    a = int(input('Введите целое число от 0 до 1000: '))
    if a == num:
        print('Число угадано')
        exit()
    elif a > num:
        print('Больше, чем заданное')
    elif a < num:
        print('Меньше, чем заданное')
    i += 1
print('Число попыток исчерпано')
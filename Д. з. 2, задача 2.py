# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions

a = str(input('Введите первую обыкновенную дробь:  '))
b = str(input('Введите вторую обыкновенную дробь:  '))
a1 = a.split(sep="/")
b1 = b.split(sep="/")
summ = int(a1[0]) / int(a1[1]) + int(b1[0]) / int(b1[1])
print(summ)
a2 = fractions.Fraction(a)
b2 = fractions.Fraction(b)
print(a2 + b2, "\n")
numerator = int(a1[0]) * int(b1[0])
denominator = int(a1[1]) * int(b1[1])
print(f'{numerator}/{denominator}')
print(a2 * b2)

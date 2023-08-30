# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

a = int(input('Введите целое число:  '))

def hexadecimal(a):
    st = ''

    while a > 0:

        if a % 16 == 10:
            st += 'A'
        elif a % 16 == 11:
            st += 'B'
        elif a % 16 == 12:
            st += 'C'
        elif a % 16 == 13:
            st += 'D'
        elif a % 16 == 14:
            st += 'E'
        elif a % 16 == 15:
            st += 'F'
        else:
            st += str(a % 16)
        a = a // 16
    return st[::-1]

print(hexadecimal(a))
print(hex(a))

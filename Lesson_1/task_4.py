# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и
# сколько между ними находится букв.

lit_1 = ord(input('Введите первую букву: '))
lit_2 = ord(input('Введите вторую букву: '))

print(f'Позиция первой буквы: {lit_1 - 96}')
print(f'Позиция второй буквы: {lit_2 - 96}')

print(f'Между буквами {abs(lit_2 - lit_1)} букв')
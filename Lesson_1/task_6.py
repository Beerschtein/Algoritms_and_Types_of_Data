# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

print('Введите длины трех отрезков\n')
a = int(input('\tПервый отрезок: '))
b = int(input('\tВторой отрезок: '))
c = int(input('\tТретий отрезок: '))

if a + b > c and a + c > b and b + c > a:
    print('\nТреугольник существует')

    if a == b and a == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or c == b:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

else:
    print('\nТреугольник не существует')
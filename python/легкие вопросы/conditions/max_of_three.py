a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))

def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(a, b, c))
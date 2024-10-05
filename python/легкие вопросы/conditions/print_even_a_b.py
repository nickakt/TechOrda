a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))

def print_even_numbers(a,b):
  for i in range(a, b + 1):
    if i % 2 == 0:
      print(i)

print_even_numbers(a,b)
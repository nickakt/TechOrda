a = int(input('Введите первое число:'))


def is_even_or_odd(a):
  if a % 2 == 0:
      print(f"The number {a} is even")
      return
  print(f"The number {a} is odd")


is_even_or_odd(a)
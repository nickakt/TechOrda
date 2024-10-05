a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))



def get_power_of_two(a,b):
  power_of_two = 1
  for i in range(b):
    power_of_two *= a
  return power_of_two



print(get_power_of_two(a,b))

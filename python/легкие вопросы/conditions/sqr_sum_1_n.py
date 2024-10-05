n = int(input('Введите первое число:'))

def get_sum_of_squares(n):
  sum_of_squares = 0
  for i in range(1,n + 1):
    sum_of_squares += i * i
  return sum_of_squares


print(get_sum_of_squares(n))

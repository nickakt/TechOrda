numbers = [7, 4, 5, 6, 7, 8, 9]


def get_min_number(numbers):
  min_number = numbers[0] 
  if len(numbers) == 0:
    return min_number
  for number in numbers:
    if number < min_number:
      min_number = number
  return min_number

print(get_min_number(numbers))
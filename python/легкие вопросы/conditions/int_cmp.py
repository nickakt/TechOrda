def get_int_cmp(a,b):
  if a > b:
    return 1
  elif a < b:
    return -1
  return 0


a = input("Введите первое число:")
b = input("Введите второе число:")

print(get_int_cmp(int(a),int(b)))
a = int(input('Введите первое число:'))


def create_list(a):
  new_list = []
  for i in range(1,a + 1):
    new_list.append(i)
  return new_list


print(create_list(a))

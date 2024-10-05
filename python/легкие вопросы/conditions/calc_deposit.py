term = int(input('Введите кол-во месяцев:'))
percent = int(input('Введите процентную ставку:'))
current_balance = int(input('Введите текущий баланс:'))


def calclulate_profit(term, percent, current_balance):
  for i in range(term):
    current_balance += current_balance / 100 * percent

  print(current_balance)


calclulate_profit(term, percent, current_balance)


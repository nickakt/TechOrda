
def is_word_palindrome(a):
  if a == a[::-1]:
    return "polidrome word"
  return "not polidrome word"


a = str(input('Введите слово:')).lower().replace('ё', 'е')

print(f"The {a} is {is_word_palindrome(a)} ")
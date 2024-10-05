from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%d.%m.%Y")
        return "Дата корректна"
    except:
        return "Дата некорректна"

date_input = str(input("Введите дату:"))
print(is_valid_date(date_input))
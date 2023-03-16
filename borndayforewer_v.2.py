import random

"""
МОДУЛЬ 2.1
Программа из 2-го дз
Реализована функция month_2_word(num_month) для преобразования номера месяца в слово
"""


def month_2_word(num_month):
    if num_month == '01':
        w_month = 'января'
    elif num_month == '02':
        w_month = 'февраля'
    elif num_month == '03':
        w_month = 'марта'
    elif num_month == '04':
        w_month = 'апреля'
    elif num_month == '05':
        w_month = 'мая'
    elif num_month == '06':
        w_month = 'июня'
    elif num_month == '07':
        w_month = 'июля'
    elif num_month == '08':
        w_month = 'августа'
    elif num_month == '09':
        w_month = 'сентября'
    elif num_month == '10':
        w_month = 'октября'
    elif num_month == '11':
        w_month = 'ноября'
    else:
        w_month = 'декабря'
    return w_month


birthdays_dict = {'Александр Пушкин': '06.06.1799',
                  'Владимир Путин': '07.10.1952',
                  'Андрей Сахаров': '21.05.1921',
                  'Никола Тесла': '10.07.1856',
                  'Стив Джобс': '24.02.1955',
                  'Михаил Лермонтов': '15.10.1814',
                  "Джеймс Кэмерон": "16.08.1954",
                  "Михаил Горбачев": "02.03.1931",
                  "Федор Достоевский": "11.11.1821",
                  "Генри Форд": "30.07.1863"
                  }
day_number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
              '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
day_name = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое",
            "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое",
            "восемнадцатое", "девятнадцатое", "двадцатое",
            "двадцать первое", "двадцать второе", "двадцать третье", "двадцать четвертое", "двадцать пятое",
            "двадцать шестое", "двадцать седьмое", "двадцать восьмое", "двадцать девятое",
            "тридцатое", "тридцать первое"]

days = dict(zip(day_number, day_name))

# Пользователь определяет кол-во вопросов для себя
qty_questions = int(input('Привет! На сколько вопросов желаете ответить? (Максимум 10) '))
# Выбираем жертв
random_people = random.sample(list(birthdays_dict.keys()), qty_questions)

correct_answers = 0
for person in random_people:
    # Получаем дату рождения для выбранных жертв
    birthday = birthdays_dict[person]
    # Предлагаем пользователю угадать дату рождения
    answer = input(f"Введите дату рождения для {person}: ")
    # Проверяем ответ
    if answer == birthday:
        print("Правильно!")
        correct_answers += 1
    else:
        month = month_2_word(birthday[3:5])

        print(
            f"Неправильно. Правильный ответ: {days[birthday[:2]]} {month} {birthday[6:]} года.")
        print()

print(f"Вы правильно ответили на {correct_answers} вопросов из {qty_questions}.")

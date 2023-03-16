"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return '*' * 10


print('return from simple_separator func \n', simple_separator())


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    for i in range(count):
        print('*', end='')
        i += 1
    return print(' <=== return from long_separator func')


long_separator(50)


# print(long_separator(3) == '***')  # True
# print(long_separator(4) == '****')  # True


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    for i in range(count):
        print(simbol, end='')
        i += 1
    return print('\n')


separator('#', 50)


# print(separator('-', 10) == '----------')  # True
# print(separator('#', 5) == '#####')  # True


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    separator('*', 3)
    print('Hello world!', '\n')
    separator('#', 5)


'''
**********

Hello World!

##########
'''
hello_world()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    separator('/', 50)
    print(f'Hello  {who} \n ')
    separator('\\', 50)


def attention_msg(msg_text):
    separator('!', 50)
    print(f'{msg_text}\n')
    separator('!', 50)


def balance_msg(msg_text):
    separator('#', 20)
    print(msg_text, '\n')
    separator('#', 20)


def purchase_list(msg_text):
    separator('|', 30)
    print(msg_text)
    separator('|', 30)


'''
**********

Hello World!

##########
'''
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    sum_args = 0
    for arg in args:
        sum_args += arg
    result = sum_args ** power
    return result


print(pow_many(1, 1, 2))  # == 3)  True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3))  # == 5)   True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1))  # == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2))  # == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4))  # == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, val in kwargs.items():
        print(f'{key} --> {val}')


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входная последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    return result


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True

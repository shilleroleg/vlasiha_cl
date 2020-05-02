#
#  Основные типы данных
#

# Числа
number_integer = 10
number_float = 10.5

result_integer = 10 * 2
result_float = 5 / 2

sum_example = 10
sum_example = sum_example + 5  # = 15
sum_example += 5  # краткая запись примера выше, аналогично с *=, /=, -= и тд

convert_to_integer = int(10.4)  # = 10
convert_to_float = float(7)  # = 7.0

simple_integer = 10000  # стандартная запись большого числа
simple_integer_readable = 10_000  # более читаемая запись большого числа

# Строки
first_name = 'John'
last_name = "Doe"  # можно использовать и ' и " для обозначения строк, предпочтительно "

full_name_simple = first_name + ' ' + last_name  # конкатенация строки (сложение)

full_name_format = f"{first_name} {last_name}"  # конкатенация строки (современный вариант)

letter = first_name[0]  # = J

first_name_slice = first_name[0:1]  # срез с 0 по 1 индексы (порядковый номер символа)

first_name_stepped_slice = first_name[0:4:2]  # срез с 0 по 4 индексы с шагом в 2

first_name_reverse = first_name[::-1]  # nhoJ


# Булево значение
is_active = True
is_disabled = False

simple_check_gt = 10 > 5  # = True
simple_check_lt = 5 < 4  # = False

convert_boolean_number = bool(10)  # True
convert_boolean_string = bool('Simple string')  # True
convert_boolean_negative = bool(-20)  # True
convert_boolean_zero = bool(0)  # False

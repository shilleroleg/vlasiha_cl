# Словари
person = {'first_name': 'John', 'age': 53}

person_construct = dict(first_name='John', age=53)

john_name_key = person['first_name']
john_name_getter = person.get('first_name')  # вернет False, если такого ключа нет

person.keys()  # вернет названия полей
person.values()  # вернет значения полей
person.items()  # вернет пары ключ-значение
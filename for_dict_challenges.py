# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name = []
name_once = []
for i in students:
    name.append(i['first_name'])
for n in name:
    if n not in name_once:
        name_once.append(n)
for n in name_once:
    counter = name.count(n)
    print(f'{n}: {counter}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name = []
for i in students:
    name.append(i['first_name'])
print(f'Самое частое имя среди учеников: {max(name, key=name.count)}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
num_class = 1
for classes in school_students:
    max_name_in_class = max(classes, key=classes.count)
    print(f'Самое частое имя в классе {num_class}: {"".join(map(str, max_name_in_class.values()))}')
    num_class += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
boys = 0
girls = 0
for classes in school:
    for students in classes['students']:
        for gender in is_male:
            if gender == students['first_name'] and is_male[gender] is False:
                girls += 1
            elif gender == students['first_name'] and is_male[gender] is True:
                boys += 1
    print(f'Класс {classes["class"]}: девочки {girls}, мальчики {boys}')
    boys = 0
    girls = 0




# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
boys = 0
girls = 0
for classes in school:
    for students in classes['students']:
        for gender in is_male:
            if gender == students['first_name'] and is_male[gender] is False:
                girls += 1
            elif gender == students['first_name'] and is_male[gender] is True:
                boys += 1
    if boys > girls:
        print(f'Больше всего мальчиков в классе {classes["class"]}')
    else:
        print(f'Больше всего девочек в классе {classes["class"]}')
    boys = 0
    girls = 0



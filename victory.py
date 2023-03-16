import random

# Задаем список известных людей и их дат рождения
people = {
    'Путина': '07.10.1952',
    'Сталина': '18.12.1878',
    'Ленина': '22.04.1870',
    'Николая II': '18.05.1868',
    'Петра I': '09.06.1672',
    'Пушкина': '26.05.1799',
    'Столыпина': '14.04.1862',
    'Жириновского': '25.04.1946',
    'Ивана Грозного': '25.08.1530',
    'Екатерины II': '02.05.1729'
}

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое'
}

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}
while True:
# счетчики правильных и неправильных ответов
    correct_answers = 0
    wrong_answers = 0

# Выбираем случайные 5 человек
    chosen_people = random.sample(list(people.keys()), 5)
    #Вопрос 1
    vopros1 = input(f'Введите дату рождения {chosen_people[0]} в формате dd.mm.yyyy: ')

    if vopros1 == people[chosen_people[0]]:

        print('Красава! Ты гений!')
        correct_answers += 1
    else:
        data = list({people[chosen_people[0]]})
        result = ' '.join(data)
        day, month, year = result.split('.')
        print(f"Позор! Правильная дата рождения {chosen_people[0]} {days[day]} {months[month]} {year} года")
        wrong_answers += 1
    # Вопрос 2
    vopros2 = input(f'Введите дату рождения {chosen_people[1]} в формате dd.mm.yyyy: ')
    if vopros2 == people[chosen_people[1]]:
        print('Красава! Ты гений!')
        correct_answers += 1
    else:
        data = list({people[chosen_people[1]]})
        result = ' '.join(data)
        day, month, year = result.split('.')
        print(f"Позор! Правильная дата рождения {chosen_people[1]} {days[day]} {months[month]} {year} года")
        wrong_answers += 1

    #Вопрос 3
    vopros3 = input(f'Введите дату рождения {chosen_people[2]} в формате dd.mm.yyyy: ')
    if vopros3 == people[chosen_people[2]]:
        print('Красава! Ты гений!')
        correct_answers += 1
    else:
        data = list({people[chosen_people[2]]})
        result = ' '.join(data)
        day, month, year = result.split('.')
        print(f"Позор! Правильная дата рождения {chosen_people[2]} {days[day]} {months[month]} {year} года")
        wrong_answers += 1
    # Вопрос 4
    vopros4 = input(f'Введите дату рождения {chosen_people[3]} в формате dd.mm.yyyy: ')
    if vopros4 == people[chosen_people[3]]:
        print('Красава! Ты гений!')
        correct_answers += 1
    else:
        data = list({people[chosen_people[3]]})
        result = ' '.join(data)
        day, month, year = result.split('.')
        print(f"Позор! Правильная дата рождения {chosen_people[3]} {days[day]} {months[month]} {year} года")
        wrong_answers += 1

    # Вопрос 5
    vopros5 = input(f'Введите дату рождения {chosen_people[4]} в формате dd.mm.yyyy: ')
    if vopros5 == people[chosen_people[3]]:
        print('Красава! Ты гений!')
        correct_answers += 1
    else:
        data = list({people[chosen_people[4]]})
        result = ' '.join(data)
        day, month, year = result.split('.')
        print(f"Позор! Правильная дата рождения {chosen_people[4]} {days[day]} {months[month]} {year} года")
        wrong_answers += 1

    # Выводим результаты
    print(f'Вы ответили правильно на {correct_answers} из 5 вопросов.')
    print(f'Вы ответили неправильно на {wrong_answers} из 5 вопросов.')


    # Предлагаем начать сначала
    answer = input('Хотите начать заново? (да/нет) ')
    if answer.lower() != 'да':
        break



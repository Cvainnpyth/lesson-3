# Задание:
# Пользователь вводит количество элементов будущего списка
# После этого по очереди по одной вводит любые цифры
# Сохранить цифры в список
# Отсортировать список по возрастанию и вывести на экран
# Пример работы: Введите количество элементов: 3
# Введите 1 элемент: 5
# Введите 2 элемент: 2
# Введите 3 элемент: 4
# Вывод: [2, 4, 5]


n = int(input("Введите количество элементов: "))

list = []
for i in range(n):
    elem = int(input(f"Введите {i+1} элемент: "))
    list.append(elem)

list.sort()


print("Вывод:", list)
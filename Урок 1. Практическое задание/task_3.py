"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

d = [
    ('q', 12),
    ('w', 133),
    ('r', 2000),
    ('z', 1),
    ('x', 3)
]

def find_max(info_list):
    """
    Сложность: #O(n log n)
    """
    info_list.sort(key=lambda i: i[1], reverse=True) #O(n log n)
    print(*info_list[:3:]) #O(1)


def find_max2(info_list):
    """
    Сложность: #O(n)
    """
    maximum = [] #O(1)
    for _ in range(3): #O(1)
        buff = 0 #O(1)
        for i in range(len(info_list)): #O(n)
            if info_list[i][1] > info_list[buff][1]: #O(1)
                buff = i #O(1)
        maximum.append(info_list.pop(buff)) #O(1)
    print(*maximum) #O(1)

"""
Первый алгоритм будет работать быстрее
"""




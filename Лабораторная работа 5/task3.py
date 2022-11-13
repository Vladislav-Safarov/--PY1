def get_unique_list_numbers(start = -10, end = 10, count = 15) -> list[int]: # TODO написать функцию для получения списка уникальных целых чисел
    from random import randint
    list_ = []
    while len(list_) != count:
        a = randint(start, end)
        if a not in list_:
            list_.append(a)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


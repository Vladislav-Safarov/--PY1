
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = list_numbers.index(max(list_numbers))
b = list_numbers[a]
list_numbers[a] = list_numbers[-1]
list_numbers[-1] = b# TODO Оформить решение

print(list_numbers)

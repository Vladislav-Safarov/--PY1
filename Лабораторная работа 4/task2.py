def get_count_char(str_):
    dict = {}
    A = 0
    for i in str_.lower():
        if i.isalpha():
            dict[i] = dict.get(i, A) + 1
    return dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
def frequency(dicts):
    for i in dicts:
        dicts[i] = round((dicts.get(i) / sum(dicts.values())) * 100, 2)
    return dicts
#print(frequency(get_count_char(main_str)))

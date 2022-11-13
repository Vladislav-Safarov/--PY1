import string
from random import sample
def get_random_password() -> str:
    number = input('количество паролей?' + "\n")
    length = input('длина пароля?' + "\n")
    if number == '':
        number = 1
    if length == '':
        length = 8
    list_pass = []
    number = int(number)
    length = int(length)
    for i in range(number):
        password = sample(list(string.ascii_lowercase + string.ascii_uppercase + string.digits), length)
        list_pass.insert(i, ''.join(password))
    return list_pass


print(get_random_password())
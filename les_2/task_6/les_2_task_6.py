# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import random

number = round(random() * 100)
try_counter = 1
print("Число было загадано, у вас 10 попыток чтобы отгадать его. Поехали!")
while try_counter <= 10:
    # user_number = int(input(str(try_counter) + '-я попытка: '))
    user_number = int(input("Введите число: "))
    print(f"Это была {try_counter}-я попытка")
    if user_number > number:
        print('Число меньше')
    elif user_number < number:
        print('Число больше')
    else:
        print(f'Вы угадали с {try_counter}-й попытки')
        break
    try_counter += 1
else:
    print(f'У вас закончились попытки. Загаданное число {number}')
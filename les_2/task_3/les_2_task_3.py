# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

number = int(input("Введите натуральное число:"))
reverse_num = 0
while number > 0:
    reverse_num = reverse_num * 10 + number % 10
    number = number // 10

print(f"Обратное число: {reverse_num}")
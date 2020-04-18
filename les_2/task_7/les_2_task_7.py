# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

number = int(input("Введите натуральное число:"))
sum_num = 0
for i in range(1, number+1):
    sum_num += i
second_num = number * (number + 1) // 2

if sum_num == second_num:
    print(f"Равенство выполняется {sum_num} = {second_num}")
else:
    print(f"Равенство не выполняется {sum_num} = {second_num}")
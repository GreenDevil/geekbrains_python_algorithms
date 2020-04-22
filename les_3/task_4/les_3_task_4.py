# 4. Определить, какое число в массиве встречается чаще всего.

from random import random

massive = 100
arr = [0] * massive
for i in range(massive):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
num_finds = 1
for i in range(massive - 1):
    find = 1
    for k in range(i + 1, massive):
        if arr[i] == arr[k]:
            find += 1
    if find > num_finds:
        num_finds = find
        num = arr[i]

if num_finds > 1:
    print(f"{num_finds} раз встречается число {num}")
else:
    print("Все элементы уникальны")
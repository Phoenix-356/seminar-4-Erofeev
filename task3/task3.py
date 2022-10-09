"""Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной 
последовательности.

*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]"""

 
from random import random 
N = 20 
a = [0] * N 
for i in range(N): 
    a[i] = int(random()*15) 
    print(a[i],end=' ') 
print() 
for i in range(N): 
    f = True 
    for j in range(N): 
        if a[i] == a[j] and i != j: 
            f = False 
            break 
    if f == True: 
        print(a[i],end=' ') 
print()
# Пиминов Аркадий ИИ-72 Уровень C
import random
import time

# Задание 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

data = [random.randint(1, 100) for _ in range(10)]
print("До:", data)
print("После:", bubble_sort(data.copy()))
print("-" * 30)

# Задание 2
N = int(input("введите размер матрицы: "))
matrix = [[random.randint(10, 99) for _ in range(N)] for _ in range(N)]

print("Исходная матрица:")
for row in matrix:
    print(row)

shifted_matrix = [matrix[-1]] + matrix[:-1]

print("\nМатрица после сдвига:")
for row in shifted_matrix: print(row)
print("-" * 30)

# Задание 3
N = int(input("введите размер матрицы: "))
for col in range(N):
    for i in range(N):
        for j in range(0, N - i - 1):
            if matrix[j][col] > matrix[j + 1][col]:
                matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]

for row in matrix:
    print(row)
print("-" * 30)

# Задание 4
large_list = [random.randint(0, 10000) for _ in range(3000)]

start_linear = time.time()
max_index = 0
for i in range(1, len(large_list)):
    if large_list[i] > large_list[max_index]:
        max_index = i
end_linear = time.time()
print(f"Метод перебора: Индекс = {max_index},"
      f"Значение = {large_list[max_index]}, Время: {end_linear - start_linear:.6f} сек")

start_bubble = time.time()
sorted_list = bubble_sort(large_list.copy())
found_max = sorted_list[-1]
original_index = large_list.index(found_max)
end_bubble = time.time()
print(f"Поиск через пузырек: Индекс = {original_index},"
      f"Значение = {found_max}, Время: {end_bubble - start_bubble:.6f} сек")

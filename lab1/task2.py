import math

# Чтение файла
with open ('lab1/files/second_task.txt', 'r', encoding='utf-8') as file:
    lines=file.readlines()
    table = []
    for line in lines:
        nums = line.strip().split(' ')
        table.append(list(map(int, nums)))

# Удаление отрицательных чисел
filtered_table = [[num for num in sublist if num > 0] for sublist in table]

# Создание списка сумм квадратных корней
sum_sqrt_row = []
for sublist in filtered_table:
    sum_sqrt = sum(math.sqrt(num) for num in sublist)
    sum_sqrt_row.append(sum_sqrt)

# Сортировка по убыванию
sum_sqrt_row.sort(reverse=True)

# Сохранение в файл
with open("lab1/files/results/task2.txt", "w") as file:
    for item in sum_sqrt_row[:10]:
            file.write(f"{item:.0f}\n")

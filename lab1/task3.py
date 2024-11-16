# Чтение файла
with open('/root/lab1/files/third_task.txt', 'r', encoding='utf-8') as file: 
    rows = file.readlines() 
 
# Создаем список для суммы строк 
row_avg = [] 
 
for row in rows: 
 
    # Разбиваем числа на int/None 
    nums = [ 
        int(num) if num != 'N/A' else None for num in row.strip().split(' ') 
    ] 
 
    # Замена None на среднее значение соседних чисел
    nums = [ 
        (nums[i - 1] + nums[i + 1]) / 2 if nums[i] is None else nums[i] 
        for i in range(len(nums)) 
    ] 
     
    # Числа, кратные двум и положительны 
    multiple_nums = [num for num in nums if num % 2 == 0 and num > 0] 
 
    # Суммы в каждой строке 
    row_avg.append(int(round((sum(multiple_nums)) / len(multiple_nums), 0)))
 
# Сохраняем файл
with open('/root/lab1/files/results/task3.txt', 'w', encoding='utf-8') as file: 
    file.write('\n'.join(map(str, row_avg)))
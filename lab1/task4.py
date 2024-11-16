import pandas as pd

# Чтение файла
df = pd.read_csv('/root/lab1/files/fourth_task.txt')

# Удаление колонки
df_dropped = df.drop('status', axis=1)

# Среднее арифметическое
mean_value = df['rating'].mean()

# Максимум
max_value = df['quantity'].max()

# Минимум
min_value = df['rating'].min()

# Фильтрация
df_filtered = df[df['price'] < 277]

# Сохранение модифицированного csv-файла
df_filtered.to_csv('/root/lab1/files/results/task4_1.csv', index=False, header=True)

# Сохранение результатов вычислений
with open("/root/lab1/files/results/task4_2.txt", "w") as file:
            file.write(f"Среднее арифметическое по столбцу rating: {mean_value}\n\
Максимальное значение по столбцу quantity: {max_value}\n\
Минимальное значение по стобцу rating: {min_value}")
import pandas as pd

# Чтение фрагмента, поиск таблиц
frag = pd.read_html('lab1/files/fifth_task.html', attrs={'id': 'product-table'}, encoding='utf-8')

# Выбор первой таблицы
table = frag[0]

# Сохранение в csv-файл
table.to_csv('lab1/files/results/task5.csv', index=False, header=True)

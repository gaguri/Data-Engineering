import requests
import pandas as pd

# Запрос данных
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

# Преобразование в датафрейм
df = pd.json_normalize(data)  # Преобразуем JSON в табличный вид

# Генерация html
html_content = df.to_html(index=False, border=1, justify="center", classes="table")

# Сохранение файла
with open('/root/lab1/files/results/task6.html', "w", encoding="utf-8") as file:
    file.write(html_content)
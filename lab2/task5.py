import pandas as pd
import os
import json

# Чтение исходного файла
df = pd.read_csv('/root/lab2/files/product_info.csv')

# Колонки, которые останутся
columns_to_save = ['product_name', 'brand_name', 'loves_count', 'rating', 'reviews', 'price_usd', 'new', 'online_only', 'out_of_stock']

# Датафрейм с выбранными колонками 
df_new = df[columns_to_save]

# Coхранение обработанных файлов
df_new.to_csv('/root/lab2/files/results/product_info_new.csv')                      #csv
df_new.to_json('/root/lab2/files/results/product_info_new.json')                    #json
df_new.to_pickle('/root/lab2/files/results/product_info_new.pkl')                   #pkl
df_new.to_pickle('/root/lab2/files/results/product_info_new.msgpack', protocol=5)   #msgpack

# Определяем размеры файлов
csv_size =  os.path.getsize('/root/lab2/files/results/product_info_new.csv')
json_size =  os.path.getsize('/root/lab2/files/results/product_info_new.json')
pkl_size = os.path.getsize('/root/lab2/files/results/product_info_new.pkl')
msgpack_size = os.path.getsize('/root/lab2/files/results/product_info_new.msgpack')

print(f'csv size = {csv_size},\n\
json size = {json_size},\n\
pickle size = {pkl_size},\n\
msgpack size = {msgpack_size},\n\
Наибольший размер - json, наименьший - csv')

# Статистика для колонок с числовыми данными
columns_stat_num = ['loves_count', 'rating', 'reviews', 'price_usd']

stat_num = {}

for col in columns_stat_num:
    stats = df_new[col].describe()
    stat_num[col] = pd.concat([stats[['min', 'max', 'mean', 'std']], pd.Series({'sum': df_new[col].sum()})]).to_dict()

# Статистика для текстовых данных
columns_stat_text = ['product_name', 'brand_name', 'new', 'online_only', 'out_of_stock']

stat_text = {}

for col in columns_stat_text:
    stat_text[col] = df_new[col].value_counts().to_dict()

# Сохранение в json
all_stats = {
    'numeric_stats': stat_num,
    'text_stats': stat_text
}

with open ('/root/lab2/files/results/task5_stats.json', 'w') as file:
    json.dump(all_stats, file, indent=1)
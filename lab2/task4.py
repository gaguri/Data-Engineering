import pickle
import json

with open ('/root/lab2/files/fourth_task_products.json', 'rb') as file:
    products = pickle.load(file)

with open ('/root/lab2/files/fourth_task_updates.json', 'r', encoding='utf-8') as file:
    products_upd = json.load(file)

product_map = {}

for product in products:
    product_map[product['name']] = product

methods = {
    'percent-': lambda price, param: price * (1 - param),
    'percent+': lambda price, param: price * (1 + param),
    'add': lambda price, param: price + param,
    'sub': lambda price, param: price - param

}

for upd in products_upd:
    product = product_map[upd['name']]
    product['price'] = methods[upd['method']](product['price'], upd['param'])

products = list(product_map.values())

with open ('/root/lab2/files/results/task4.pkl', 'wb') as file:
    pickle.dump(products, file)
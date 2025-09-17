# Список покупок
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Общая выручка
def total_revenue(array: list) -> float:
    count_all = 0
    for i in array:
        count_all += i['price'] * i['quantity']
    return count_all

# Уникальные товары категории
def item_by_category(array: list) -> dict:
    item_category = {}
    for i in array:
        item_category.setdefault(i['category'], []).append(i['item'])
    return item_category

# Минимальный прайс
def mp(array: list) -> float:
    min_p = 1000
    for i in array:
        if i['price'] < min_p:
            min_p = i['price']
    return min_p

# Цена больше или равна минимальному прайсу
def expensive_purchases(array: list, min_price: float) -> list:
    list_price = []
    for i in array:
        if i['price'] > min_price:
            list_price.append(i)
    return list_price

# Средняя цена товаров по каждой категории
def average_price_by_category(array: list) -> dict:
    avg_dict = {}
    for i in array:
        avg_dict.setdefault(i['category'],[]).append(i['price'])

    for key, values in avg_dict.items():
        avg_dict[key] = sum(values) / len(values)

    return avg_dict

# Категория с наибольшим количеством купленных товаров
def most_frequent_category(array: list) -> dict:
    max_quantity = {}
    for i in array:
        max_quantity.setdefault(i['category'],[]).append(i['quantity'])

    total_quantity = 0
    name_category = ''
    for key, values in max_quantity.items():
        if sum(values) > total_quantity:
            total_quantity = sum(values)
            name_category = key
    return name_category


# Вызов всех функций
def main():
    print(f'Общая выручка: {total_revenue(purchases)}')
    print(f'Товары по категориям: {item_by_category(purchases)}')
    print(f'Покупки дороже {mp(purchases)}: {expensive_purchases(purchases, mp(purchases))}')
    print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
    print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')

main()







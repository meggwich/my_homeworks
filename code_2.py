cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция для создания списка покупок по списку блюд и количеству персон.

    Параметры:
    dishes (list): Список блюд.
    person_count (int): Количество персон.

    Возвращает:
    shop_list (dict): Словарь с названием ингредиентов и его количества для блюда.
    """

    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            # Если ингредиент уже есть в списке покупок, увеличиваем его количество
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            # Если ингредиента нет в списке покупок, добавляем его
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}

    return shop_list
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count)

print(shop_list)
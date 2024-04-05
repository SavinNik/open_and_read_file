from pprint import pprint


# Задание №1
def load_file():
    with open('recipes.txt') as file:
        cook_book = {}
        for row in file:
            dish = row.strip()
            ingredients_count = int(file.readline())
            ingredient_list = []
            for item in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip('\n').split(' | ')
                ingredient_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish] = ingredient_list
            file.readline()
    return cook_book


# Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingredients = load_file()
    for dish in dishes:
        if dish in ingredients:
            for ingredient in ingredients[dish]:
                if shop_list.values() in ingredient:
                    shop_list[ingredient['ingredient_name']] += {'measure': ingredient['measure'],
                                                                 'quantity': int(ingredient['quantity']) * person_count}
                elif ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] = \
                        int(shop_list[ingredient['ingredient_name']]['quantity']) + (
                                    int(ingredient['quantity']) * person_count)
                else:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': int(ingredient['quantity']) * person_count}
    return shop_list


pprint(load_file())
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))


# Задание №3
file_names = ['1.txt', '2.txt', '3.txt']

open_files_list = []

for file_ in file_names:
    with open(file_) as f:
        file_list = []
        file_lines = f.readlines()
        len_lines = len(file_lines)
        file_list += len_lines, file_, file_lines
        open_files_list.append(file_list)

open_files_list.sort()

with open('result_file.txt', 'w') as f:
    for row_ in open_files_list:
        f.write(row_[1])
        f.write('\n')
        f.write(str(row_[0]))
        f.write('\n')
        for i in row_[2]:
            f.write(i)
        f.write('\n')

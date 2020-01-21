from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import argparse

FOUNDATION_YEAR = 1920


def split_line(line):
    synonym_dict = {'Название': 'name',
                    'Сорт': 'grape_sort',
                    'Цена': 'price',
                    'Картинка': 'image',
                    'Выгодное предложение': 'special_offer'}

    try:
        key, val = line.split(':')
        key = key.strip()
        val = val.strip()
    except ValueError:
        key = line.strip()
    if key in synonym_dict:
        key = synonym_dict[key]
    if key == 'special_offer':
        val = True

    return key, val


def get_drinks_assortment(file_lines):
    drinks_assortment = dict()
    drink_characteristics = dict()
    wine_sort = ''
    num_of_file_lines = len(file_lines)
    for line_counter, line in enumerate(file_lines, 1):
        if '#' in line:
            if drink_characteristics:
                drinks_assortment[wine_sort].append(drink_characteristics)
                drink_characteristics = dict()
            _, wine_sort = line.split('#')
            wine_sort = wine_sort.strip()
            drinks_assortment[wine_sort] = []
        elif line != '\n' and line_counter != num_of_file_lines:
            key, value = split_line(line)
            if key not in drink_characteristics:
                drink_characteristics[key] = value
            else:
                drinks_assortment[wine_sort].append(drink_characteristics)
                drink_characteristics = dict()
                drink_characteristics[key] = value
        elif line != '\n' and line_counter == num_of_file_lines:
            key, value = split_line(line)
            drink_characteristics[key] = value
            drinks_assortment[wine_sort].append(drink_characteristics)

    return drinks_assortment


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()
    text_file = args.file_name
    
    current_date = datetime.now()
    vinery_age = current_date.year - FOUNDATION_YEAR

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    with open(text_file, encoding='utf-8-sig') as file:
        file_lines = file.readlines()
        
    drinks_assortment = get_drinks_assortment(file_lines)
    
    rendered_page = template.render(
        vinery_age=vinery_age,
        drinks_assortment=drinks_assortment
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

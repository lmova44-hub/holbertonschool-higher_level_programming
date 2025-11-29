#!/usr/bin/python3
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Если файл существует — загружаем, иначе создаём пустой список
if path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

# Добавляем аргументы командной строки (кроме имени скрипта)
items.extend(sys.argv[1:])

# Сохраняем обновлённый список
save_to_json_file(items, filename)

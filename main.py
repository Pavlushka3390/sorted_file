import os
from pathlib import Path


path = os.getcwd()
directory = [f for f in os.listdir(path) if f.endswith('.txt')]
def get_size(file_name):
    doc_size = {}
    for name in file_name:
        with open(f'{name}', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip() != '']
        doc_size[name] = len(lines)
    sorted_document = {}
    sorted_doc = sorted(doc_size, key=doc_size.get)
    for item in sorted_doc:
        sorted_document[item] = doc_size[item]
    return sorted_document


def create_file(name_file):
    with open(f'{name_file}', 'w+', encoding='utf-8') as file:
       file.write('')

create_file('4.txt')

def write_file(file):
    dict_ = get_size(directory)
    lst_key = []
    lst_value = []
    for key, value in dict_.items():
        lst_key.append(key)
        lst_value.append(value)
    for i in range(len(lst_key)):
        with open(f'{lst_key[0]}', 'a', encoding='utf-8') as second, open(f'{lst_key[i+1]}', encoding='utf-8') as first:
            data = first.read()
            second.write(f'{lst_key[i+1]}\n')
            second.write(f'{lst_value[i+1]}\n')
            second.write(f'{data}\n')
            second.write('\n')

write_file(create_file('4.txt'))



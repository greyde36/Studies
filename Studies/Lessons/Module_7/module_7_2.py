def custom_write(file_name, strings):
    file_name = 'text_module7_2.text'
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    for i, strings in enumerate(strings):
        strings_position[(i + 1, file.tell())] = strings
        file.write(strings + '\n')
    file.close()
    return strings_position


info = ['Text for tell.', 'Используйте кодировку utf-8.',
        'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
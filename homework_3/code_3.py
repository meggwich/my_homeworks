def merge_files_alt(file_list, output_file):
    # Создаем список для хранения пар (количество строк, содержимое файла)
    files_content = []

    for fname in file_list:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.readlines()
            files_content.append((len(content), fname, content))

    # Сортируем список по количеству строк
    files_content.sort()

    with open(output_file, 'w', encoding='utf-8') as f:
        for lines_count, fname, content in files_content:
            f.write('\n' + fname + '\n')  # добавляем новую строку перед именем файла
            f.write(str(lines_count) + '\n')
            f.writelines(content)
# Список файлов для объединения
file_list = ['1.txt', '2.txt', '3.txt']

# Имя итогового файла
output_file = 'merged.txt'

# Вызов функции для объединения файлов
merge_files_alt(file_list, output_file)
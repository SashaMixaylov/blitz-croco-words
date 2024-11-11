# Задача 2024.11.01.02
#
# В какой контейнер данных нужно собирать слова чтобы исключить дубликаты?
# Поменяйте код так, чтобы это сделать.
#
# Подумайте на каком уровне лучше это делать и почему.
#
# Напишите сколько было слов всего из всех файлов, когда вы сохраняли их в список, и сколько стало, когда вы исключили дубликаты.

# Задача 2024.11.01.03
#
# Продолжаем рефакторить код: вынесите проверку валидности строки, получаемой из презентации, в отдельную функцию.

import zipfile
from pathlib import Path
import os
from second_file import extract


zip_name = "croco-blitz-source.zip"

def parsing(name):
    with zipfile.ZipFile(Path(os.path.dirname(os.path.realpath(__file__))) / 'src' / name) as archive:
        presentation_files = [file for file in archive.namelist() if file.endswith('.pptx')]

        unique_words = set()

        for words in extract(presentation_files):
            for i in range(len(words)):
                if words[i] not in unique_words:
                    unique_words.append(words[i])

            for i in range(len(words)):
                print(f"{i + 1} {words[i]}")

            for i in range(len(unique_words)):
                print(f"{i + 1} без дубликотов {len(unique_words[i])}")

if __name__ == '__main__':
    parsing(zip_name)

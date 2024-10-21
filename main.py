# Задача 2024.10.21.03
#
# Создать в репозиторие файл main.py
#
# Вывести на экран путь к директории, где лежит файл main.py
#
# Закоммитить, приложить скрин и коммит.

import os
import sys
import zipfile
from pathlib import Path

print(os.path.dirname(os.path.abspath(sys.argv[0])))  # путь где лежит файл main.py

zip = "croco-blitz-source.zip"
def see():
    folder = os.path.dirname(os.path.realpath(__file__))
    try:
        with zipfile.ZipFile(Path(folder) / 'src' / zip) as archive:
            for n in archive.namelist():
                print(n)
    except zipfile.BadZipFile as archive:
        print("error")

if __name__ == '__main__':
    see()

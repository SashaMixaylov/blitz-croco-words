# Задача 2024.10.21.03
#
# Создать в репозиторие файл main.py
#
# Вывести на экран путь к директории, где лежит файл main.py
#
# Закоммитить, приложить скрин и коммит.

import os
import sys

print(os.path.dirname(os.path.abspath(sys.argv[0])))
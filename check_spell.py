# Задача 2024.10.11.04
#
# Напишите простую программу check_spell.py
#
# Которая отправляет на проверку строку Колакал малако и получает исправленный вариант обратно.
#
# Пришлите код и скриншот.

import pyaspeller
from  pyaspeller import YandexSpeller

def chec_spell(w):
    return pyaspeller.YandexSpeller().spelled(w)


if __name__ == '__main__':
    print(chec_spell("Колакал малако"))
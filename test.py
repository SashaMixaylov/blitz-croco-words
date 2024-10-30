import pytest


#from task_04 import one_word

# Задача 2024.10.30.02
#
# Напишите тест, который проверяет, что в строке находится всего одно слово.

# Задача 2024.10.30.03
#
# Напишите тест, который проверяет, что в списке находятся только строки, состоящие из одного слова, без пробелов, цифр или знаков препинания.

# def test_one_word(capsys):
#     test1 = ["Привет"]
#     result = one_word("Привет")
#     assert test1 == result
#
# def test_one_word1(capsys):
#     test2 = ["Привет"]
#     result = one_word("Привет Всем")
#     assert test2 != result


def work(w: str) -> bool:
    return w.isalpha()


def tests():
    assert work("string") == True
    assert work("string ") == False
    assert work("string.") == False
    assert work("string2") == False
    assert work("") == False


def test_words():
    with open("words.txt", 'r', encoding='utf-8') as f:
        for i in f:
            assert work(i.strip()) == True

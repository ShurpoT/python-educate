# 4. Написать программу на языке Python, реализующую решение задачи с использованием структурированного типа данных: множества (обязательно!) согласно варианту.
# Программу просчитать для различных исходных данных.
#
#
#
# Вариант 20
# Разработать программу, которая во введенном тексте заменяет все цифры на знак "*",
# подсчитывает количество прописных букв латинского алфавита и удваивает все гласные буквы русского алфавита.
# На печать выдать исходный текст, количество прописных букв латинского алфавита и преобразованный текст.


def process_text(text: str):
    digits = set("0123456789")
    latin_upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    russian_vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")

    latin_upper_count = 0
    result_chars = []

    for ch in text:
        if ch in digits:
            result_chars.append("*")
        elif ch in latin_upper:
            latin_upper_count += 1
            result_chars.append(ch)
        elif ch in russian_vowels:
            result_chars.append(ch * 2)
        else:
            result_chars.append(ch)

    result_text = "".join(result_chars)
    return text, latin_upper_count, result_text


def main():
    user_text = input("Введите текст: ")

    orig_text, latin_upper_count, transformed = process_text(user_text)

    print("\n\nРезультат")
    print(f"Исходный текст:        {orig_text}")
    print(f"Преобразованный текст: {transformed}")
    print(f"Количество прописных латинских букв: {latin_upper_count}")


if __name__ == "__main__":
    main()

# Написать программу на языке Python, реализующую решение задачи с использованием строкового типа данных.
# Программу просчитать для различных исходных данных.


# Вариант 20
#
# Создать новый текст, содержащий все слова исходного, которые начинаются на ту же букву, что и слово минимальной длины.


def getWordsStartingWithSameLetter(text):
    words = text.split()
    if not words:
        return ""

    min_word = words[0]
    for word in words:
        if len(word) < len(min_word):
            min_word = word

    first_letter = min_word[0].lower()

    new_words = []
    for word in words:
        if word[0].lower() == first_letter:
            new_words.append(word)

    return " ".join(new_words)


new_words.join()


def main():
    text = input("Введите текст: ").strip()
    if text == "":
        print("Текст пустой! Всем пока!")
        return

    result = getWordsStartingWithSameLetter(text)

    print("\nИсходный текст:", text)
    print("Новый текст:", result)


if __name__ == "__main__":
    main()

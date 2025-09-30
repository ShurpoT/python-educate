# Написать программу на языке Python, создающую из русско-английского словаря англо-русский словарь (обязательно использовать словари(dict)).
#   - Входные данные берутся из файла input.txt, выходные данные записываются в файл output.txt.
#   - Входные данные лексикографически отсортированы, и вы-ходные данные тоже должны быть отсортированы! В выходной файл пер-вым записать полученное количество английских слов!
#   - Необходимо, чтобы во входном файле находилось, как минимум, 5 русских слов, которые имеют несколько английских значений.
#
#  На хорошую оценку по работе (8, 9 и 10) слова должны быть подобраны так, как в моём примере, чтобы в результате одно английское слово имело несколько русских значений

encoding = "utf-8"


def read_ru_en(filename):
    ru_en = {}
    with open(filename, "r", encoding=encoding) as f:
        lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        if not line or "-" not in line:
            continue
        ru_w, en_part = line.split("-", 1)
        ru_w = ru_w.strip()
        en_words = [w.strip() for w in en_part.split(",") if w.strip()]
        if ru_w in ru_en:
            ru_en[ru_w].extend(en_words)
        else:
            ru_en[ru_w] = en_words
    return ru_en


def invert_dict(ru_en):
    en_ru = {}
    for ru_w, eng_list in ru_en.items():
        for en_w in eng_list:
            if en_w not in en_ru:
                en_ru[en_w] = set()
            en_ru[en_w].add(ru_w)
    return en_ru


def write_eng_rus(filename, en_ru):
    sorted_eng = sorted(en_ru.keys())
    with open(filename, "w", encoding=encoding) as f:
        f.write(f"{len(sorted_eng)}\n")

        for en_w in sorted_eng:
            ru_words = sorted(en_ru[en_w])
            f.write(f"{en_w} - {', '.join(ru_words)}\n")


def main():
    input_file = f""
    output_file = f""

    ru_en = read_ru_en(input_file)
    en_ru = invert_dict(ru_en)
    write_eng_rus(output_file, en_ru)
    print("Cловарь создан!")


if __name__ == "__main__":
    main()

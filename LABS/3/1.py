# Разработанные во втором задании программы оформить, с использованием пользовательских функций.
# Обработать все возможные (по возможности) ошибки пользовательского ввода.

# Вариант 20


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: нужно ввести целое число!")


def input_vector():
    while True:
        n = input_int("длина вектора(списка) = ")
        if n > 0:
            break
        print("Ошибка: длина должна быть положительным числом!")

    arr = []
    for i in range(n):
        value = input_int(f"arr[{i}] = ")
        arr.append(value)
    return arr


def count_min_occurrences(arr):
    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
    count = arr.count(min_val)
    return min_val, count


def main():
    arr = input_vector()
    min_val, count = count_min_occurrences(arr)

    print("\n\n")
    print(f"_list: {arr}")
    print(f"min: {min_val}")
    print(f"minCount: {count}")


if __name__ == "__main__":
    main()

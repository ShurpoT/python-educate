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


def find_odd_max(arr):
    odd_max = None
    for x in arr:
        if x % 2 != 0:
            if odd_max is None or x > odd_max:
                odd_max = x
    return odd_max


def count_even(arr):
    even_count = 0
    for x in arr:
        if x % 2 == 0:
            even_count += 1
    return even_count


def main():
    arr = input_vector()
    odd_max = find_odd_max(arr)
    even_count = count_even(arr)

    print("\n\n")
    print(f"_list: {arr}")
    if odd_max is not None:
        print(f"oddMax: {odd_max}")
    else:
        print("В векторе нет нечётных чисел")
    print(f"evenCount: {even_count}")


if __name__ == "__main__":
    main()

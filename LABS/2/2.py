# На языке Python 3 разработать 2 программы (модули) для обработки одно-мерных массивов (векторов), используя списки.
# Одна программа должна работать с целочисленным вектором, а вторая с вещественным вектором.

# Вариант 20
# 20.   2) Дан целочисленный вектор А(n). Найти наибольшее из нечетных и количество четных чисел вектора. На печать выдавать исходный вектор и полученный результат.

_list = []
listLength = int(input("длина вектора(списка) = "))
evenCount = 0

oddMax = 1

for i in range(listLength):
    value = int(input(f"arr[{i}] = "))
    _list.append(value)


for i in range(listLength):
    if _list[i] > oddMax and _list[i] % 2 != 0:
        oddMax = _list[i]

for i in range(listLength):
    if _list[i] % 2 == 0:
        evenCount = evenCount + 1


print("\n\n")
print(f"_list: {_list}")
print(f"oddMax: {oddMax}")
print(f"evenCount: {evenCount}")

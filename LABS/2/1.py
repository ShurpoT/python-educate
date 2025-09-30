# На языке Python 3 разработать 2 программы (модули) для обработки одно-мерных массивов (векторов), используя списки.
# Одна программа должна работать с целочисленным вектором, а вторая с вещественным вектором.

# Вариант 20
# 20.   1) Дан целочисленный вектор А(n). Подсчитать сколько раз встречается в этом векто-ре минимальное по величине число.


_list = []
listLength = int(input("длина вектора(списка) = "))

for i in range(listLength):
    value = int(input(f"arr[{i}] = "))
    _list.append(value)

min = _list[0]
minCount = 0

for i in range(listLength - 1):
    if _list[i] < min:
        min = _list[i]

for i in range(listLength):
    if _list[i] == min:
        minCount = minCount + 1


print("\n\n")
print(f"_list: {_list}")
print(f"min: {min}")
print(f"minCount: {minCount}")

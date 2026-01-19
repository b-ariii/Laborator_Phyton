numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Находим индекс пропущенного элемента (None)
none_index = numbers.index(None)
# Создаем копию списка без None для вычисления суммы
numbers_without_none = [num for num in numbers if num is not None]
# Вычисляем сумму всех элементов кроме None
total_sum = sum(numbers_without_none)
# Вычисляем среднее арифметическое
# Количество элементов включает None (по условию)
count = len(numbers)
average = total_sum / (count - 1)  # делим на (количество всех элементов - 1)
# Округляем до 2 знаков после запятой с помощью format
average = float(f"{average:.2f}")
# Заменяем None на среднее арифметическое
numbers[none_index] = average
print("Измененный список:", numbers)

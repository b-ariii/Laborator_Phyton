# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    # Разделяем строки на списки участников
    list1 = first_group.split(separator)
    list2 = second_group.split(separator)
# Находим общих участников
    common_participants = set(list1).intersection(set(list2))
    return sorted(list(common_participants))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)

print(f"Общие участники: {common_participants}")
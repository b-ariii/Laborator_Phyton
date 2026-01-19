list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# Определяем общее количество игроков в списке
total_players = len(list_players)
print(f"Общее количество игроков: {total_players}")
# индекс середины
middle_index = total_players // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)

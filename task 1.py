import json

# TODO решите задачу
def task() -> float:
    # Читаем данные из файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений score * weight для каждого элемента
    total = sum(item["score"] * item["weight"] for item in data)

    # Округляем до 3 знаков после запятой
    return round(total, 3)


if __name__ == '__main__':
    print(task())

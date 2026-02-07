"""
Модуль с тремя классами, описывающими различные объекты
"""

from typing import List


class Dog:
    """
    Класс, представляющий собаку.

    Атрибуты:
        name (str): Кличка собаки
        age (int): Возраст собаки в годах
        breed (str): Порода собаки
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализирует собаку.

        Args:
            name: Кличка собаки
            age: Возраст собаки (должен быть >= 0)
            breed: Порода собаки

        Raises:
            ValueError: Если возраст отрицательный
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.name = name
        self.age = age
        self.breed = breed

    def bark(self) -> str:
        """
        Собака лает.

        Returns:
            str: Звук лая
        """

    def get_human_age(self) -> int:
        """
        Получить возраст собаки в человеческих годах.

        Returns:
            int: Примерный возраст в человеческих годах
        """

    def play(self) -> str:
        """
        Собака играет.

        Returns:
            str: Описание игры
        """


class Car:
    """
    Класс, представляющий автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля
        model (str): Модель автомобиля
        fuel_level (int): Уровень топлива в процентах (0-100)
    """

    def __init__(self, brand: str, model: str, fuel_level: int = 100):
        """
        Инициализирует автомобиль.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            fuel_level: Уровень топлива (0-100)

        Raises:
            ValueError: Если уровень топлива не в диапазоне 0-100
        """
        if not 0 <= fuel_level <= 100:
            raise ValueError("Уровень топлива должен быть от 0 до 100%")

        self.brand = brand
        self.model = model
        self.fuel_level = fuel_level

    def drive(self, distance: int) -> bool:
        """
        Проехать заданное расстояние.

        Args:
            distance: Расстояние в километрах

        Returns:
            bool: True если поездка успешна, False если не хватило топлива
        """

    def refuel(self, amount: int) -> None:
        """
        Заправить автомобиль.

        Args:
            amount: Количество топлива в процентах

        Raises:
            ValueError: Если количество не в диапазоне 1-100
        """

    def honk(self) -> str:
        """
        Подать звуковой сигнал.

        Returns:
            str: Звук сигнала
        """


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
        name (str): Имя студента
        student_id (str): Номер студенческого билета
        grades (List[int]): Список оценок
    """

    def __init__(self, name: str, student_id: str):
        """
        Инициализирует студента.

        Args:
            name: Имя студента
            student_id: Номер студенческого билета
        """
        self.name = name
        self.student_id = student_id
        self.grades: List[int] = []

    def add_grade(self, grade: int) -> bool:
        """
        Добавить оценку студенту.

        Args:
            grade: Оценка (должна быть от 2 до 5)

        Returns:
            bool: True если оценка добавлена

        Raises:
            ValueError: Если оценка не в диапазоне 2-5
        """

    def get_average_grade(self) -> float:
        """
        Получить средний балл студента.

        Returns:
            float: Средний балл
        """

    def study(self, subject: str) -> str:
        """
        Студент изучает предмет.

        Args:
            subject: Название предмета

        Returns:
            str: Сообщение об изучении предмета
        """


if __name__ == "__main__":
    # Создаем экземпляры классов
    dog = Dog("Шарик", 3, "овчарка")
    car = Car("Toyota", "Camry", 80)
    student = Student("Иван", "ST12345")

    # Выводим информацию об объектах
    print(f"Собака: {dog.name}, {dog.age} лет, порода: {dog.breed}")
    print(f"Автомобиль: {car.brand} {car.model}, топливо: {car.fuel_level}%")
    print(f"Студент: {student.name}, номер билета: {student.student_id}")

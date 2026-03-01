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

    Примеры:
        >>> dog = Dog("Шарик", 3, "овчарка")
        >>> dog.name
        'Шарик'
        >>> dog.age
        3
        >>> dog.breed
        'овчарка'
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

        Примеры:
            >>> dog = Dog("Шарик", 3, "овчарка")
            >>> Dog("Бобик", -1, "дворняга")
            Traceback (most recent call last):
            ...
            ValueError: Возраст не может быть отрицательным
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

        Примеры:
            >>> dog = Dog("Шарик", 3, "овчарка")
            >>> dog.bark()
            'Гав-гав!'
        """
        return "Гав-гав!"

    def get_human_age(self) -> int:
        """
        Получить возраст собаки в человеческих годах.

        Returns:
            int: Примерный возраст в человеческих годах

        Примеры:
            >>> dog = Dog("Шарик", 3, "овчарка")
            >>> dog.get_human_age()
            21
            >>> dog = Dog("Бобик", 1, "дворняга")
            >>> dog.get_human_age()
            7
        """
        return self.age * 7

    def play(self) -> str:
        """
        Собака играет.

        Returns:
            str: Описание игры

        Примеры:
            >>> dog = Dog("Шарик", 3, "овчарка")
            >>> dog.play()
            'Собака бегает за мячиком'
        """
        return "Собака бегает за мячиком"


class Car:
    """
    Класс, представляющий автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля
        model (str): Модель автомобиля
        fuel_level (int): Уровень топлива в процентах (0-100)

    Примеры:
        >>> car = Car("Toyota", "Camry", 80)
        >>> car.brand
        'Toyota'
        >>> car.model
        'Camry'
        >>> car.fuel_level
        80
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

        Примеры:
            >>> car = Car("Toyota", "Camry", 80)
            >>> Car("Toyota", "Camry", 150)
            Traceback (most recent call last):
            ...
            ValueError: Уровень топлива должен быть от 0 до 100%
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

        Примеры:
            >>> car = Car("Toyota", "Camry", 50)
            >>> car.drive(30)
            True
            >>> car.fuel_level
            20
            >>> car.drive(30)
            False
            >>> car.fuel_level
            20
        """
        # Расход топлива: 1% на 1 км
        fuel_needed = distance

        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            return True
        return False

    def refuel(self, amount: int) -> None:
        """
        Заправить автомобиль.

        Args:
            amount: Количество топлива в процентах

        Raises:
            ValueError: Если количество не в диапазоне 1-100

        Примеры:
            >>> car = Car("Toyota", "Camry", 30)
            >>> car.refuel(20)
            >>> car.fuel_level
            50
            >>> car.refuel(200)
            Traceback (most recent call last):
            ...
            ValueError: Количество топлива должно быть от 1 до 100
        """
        if not 1 <= amount <= 100:
            raise ValueError("Количество топлива должно быть от 1 до 100")

        new_level = self.fuel_level + amount
        if new_level > 100:
            self.fuel_level = 100
        else:
            self.fuel_level = new_level

    def honk(self) -> str:
        """
        Подать звуковой сигнал.

        Returns:
            str: Звук сигнала

        Примеры:
            >>> car = Car("Toyota", "Camry")
            >>> car.honk()
            'Бип-бип!'
        """
        return "Бип-бип!"


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
        name (str): Имя студента
        student_id (str): Номер студенческого билета
        grades (List[int]): Список оценок

    Примеры:
        >>> student = Student("Иван", "ST12345")
        >>> student.name
        'Иван'
        >>> student.student_id
        'ST12345'
        >>> student.grades
        []
    """

    def __init__(self, name: str, student_id: str):
        """
        Инициализирует студента.

        Args:
            name: Имя студента
            student_id: Номер студенческого билета

        Примеры:
            >>> student = Student("Иван", "ST12345")
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

        Примеры:
            >>> student = Student("Иван", "ST12345")
            >>> student.add_grade(5)
            True
            >>> student.grades
            [5]
            >>> student.add_grade(1)
            Traceback (most recent call last):
            ...
            ValueError: Оценка должна быть от 2 до 5
        """
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть от 2 до 5")

        self.grades.append(grade)
        return True

    def get_average_grade(self) -> float:
        """
        Получить средний балл студента.

        Returns:
            float: Средний балл

        Примеры:
            >>> student = Student("Иван", "ST12345")
            >>> student.add_grade(5)
            True
            >>> student.add_grade(4)
            True
            >>> student.add_grade(5)
            True
            >>> student.get_average_grade()
            4.67
            >>> student = Student("Петр", "ST67890")
            >>> student.get_average_grade()
            0.0
        """
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def study(self, subject: str) -> str:
        """
        Студент изучает предмет.

        Args:
            subject: Название предмета

        Returns:
            str: Сообщение об изучении предмета

        Примеры:
            >>> student = Student("Иван", "ST12345")
            >>> student.study("Математика")
            'Иван изучает Математика'
        """
        return f"{self.name} изучает {subject}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Создаем экземпляры классов
    dog = Dog("Шарик", 3, "овчарка")
    car = Car("Toyota", "Camry", 80)
    student = Student("Иван", "ST12345")

    # Выводим информацию об объектах
    print(f"Собака: {dog.name}, {dog.age} лет, порода: {dog.breed}")
    print(f"Автомобиль: {car.brand} {car.model}, топливо: {car.fuel_level}%")
    print(f"Студент: {student.name}, номер билета: {student.student_id}")
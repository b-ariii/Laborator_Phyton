from abc import ABC, abstractmethod
from typing import Optional


class Vehicle(ABC):
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        _brand (str): Марка транспортного средства (непубличный)
        _model (str): Модель транспортного средства (непубличный)
        _year (int): Год выпуска (непубличный)
        mileage (float): Пробег в километрах
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0):
        """
        Инициализирует транспортное средство.

        Args:
            brand: Марка транспортного средства
            model: Модель транспортного средства
            year: Год выпуска
            mileage: Начальный пробег (по умолчанию 0)

        Raises:
            ValueError: Если год выпуска некорректный или пробег отрицательный
        """
        if year < 1900 or year > 2024:
            raise ValueError("Год выпуска должен быть между 1900 и 2024")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")

        self._brand = brand  # Инкапсуляция: защищаем от прямого изменения
        self._model = model  # Инкапсуляция: защищаем от прямого изменения
        self._year = year  # Инкапсуляция: защищаем от прямого изменения
        self.mileage = mileage  # Публичный атрибут, может быть изменен

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self._brand} {self._model} ({self._year} г.)"

    def __repr__(self) -> str:
        """Возвращает валидную строку для инициализации такого же экземпляра."""
        return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, year={self._year}, mileage={self.mileage})"

    def get_info(self) -> str:
        """
        Возвращает полную информацию о транспортном средстве.

        Returns:
            str: Информация о транспортном средстве
        """
        return f"ТС: {self._brand} {self._model}, {self._year} г., пробег: {self.mileage} км"

    def drive(self, distance: float) -> str:
        """
        Метод для поездки на транспортном средстве.

        Args:
            distance: Расстояние поездки в километрах

        Returns:
            str: Сообщение о поездке

        Raises:
            ValueError: Если расстояние отрицательное
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")

        self.mileage += distance
        return f"Проехали {distance} км. Общий пробег: {self.mileage} км"

    @abstractmethod
    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Абстрактный метод для расчета стоимости топлива.
        Должен быть переопределен в дочерних классах.

        Args:
            distance: Расстояние в километрах
            fuel_price: Цена топлива за литр

        Returns:
            float: Стоимость топлива для поездки
        """
        pass


class PassengerCar(Vehicle):
    """
    Класс легкового автомобиля, наследующийся от Vehicle.

    Дополнительные атрибуты:
        _body_type (str): Тип кузова (седан, хэтчбек, универсал и т.д.)
        _fuel_consumption (float): Расход топлива (л/100 км)
        passenger_count (int): Количество пассажиров
    """

    def __init__(self, brand: str, model: str, year: int, body_type: str,
                 fuel_consumption: float, mileage: float = 0, passenger_count: int = 0):
        """
        Инициализирует легковой автомобиль.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            body_type: Тип кузова
            fuel_consumption: Расход топлива (л/100 км)
            mileage: Начальный пробег
            passenger_count: Количество пассажиров
        """
        # Вызываем конструктор родительского класса
        super().__init__(brand, model, year, mileage)

        self._body_type = body_type  # Инкапсуляция: защищаем от прямого изменения
        self._fuel_consumption = fuel_consumption  # Инкапсуляция: защищаем от прямого изменения
        self.passenger_count = passenger_count  # Публичный атрибут

    def __str__(self) -> str:
        """Перегруженный метод для легкового автомобиля."""
        return f"Легковой автомобиль: {self._brand} {self._model} ({self._year} г.), кузов: {self._body_type}"

    def __repr__(self) -> str:
        """Перегруженный метод для легкового автомобиля."""
        return (f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, "
                f"year={self._year}, body_type={self._body_type!r}, "
                f"fuel_consumption={self._fuel_consumption}, mileage={self.mileage}, "
                f"passenger_count={self.passenger_count})")

    def get_info(self) -> str:
        """
        Перегруженный метод для получения информации о легковом автомобиле.

        Причина перегрузки: Необходимо добавить информацию о типе кузова и расходе топлива.

        Returns:
            str: Расширенная информация о легковом автомобиле
        """
        base_info = super().get_info()
        return f"{base_info}, кузов: {self._body_type}, расход: {self._fuel_consumption} л/100км, пассажиров: {self.passenger_count}"

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Реализация абстрактного метода для расчета стоимости топлива.

        Args:
            distance: Расстояние в километрах
            fuel_price: Цена топлива за литр

        Returns:
            float: Стоимость топлива для поездки
        """
        fuel_needed = (distance / 100) * self._fuel_consumption
        return round(fuel_needed * fuel_price, 2)

    def add_passenger(self) -> str:
        """
        Унаследованный и адаптированный метод для добавления пассажира.

        Returns:
            str: Сообщение о добавлении пассажира
        """
        self.passenger_count += 1
        return f"Пассажир добавлен. Всего пассажиров: {self.passenger_count}"


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследующийся от Vehicle.

    Дополнительные атрибуты:
        _capacity (float): Грузоподъемность в тоннах
        _fuel_consumption_empty (float): Расход топлива без груза (л/100 км)
        _fuel_consumption_loaded (float): Расход топлива с грузом (л/100 км)
        cargo_weight (float): Текущий вес груза в тоннах
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float,
                 fuel_consumption_empty: float, fuel_consumption_loaded: float,
                 mileage: float = 0, cargo_weight: float = 0):
        """
        Инициализирует грузовой автомобиль.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            capacity: Грузоподъемность в тоннах
            fuel_consumption_empty: Расход топлива без груза (л/100 км)
            fuel_consumption_loaded: Расход топлива с грузом (л/100 км)
            mileage: Начальный пробег
            cargo_weight: Текущий вес груза в тоннах
        """
        # Вызываем конструктор родительского класса
        super().__init__(brand, model, year, mileage)

        self._capacity = capacity  # Инкапсуляция: защищаем от прямого изменения
        self._fuel_consumption_empty = fuel_consumption_empty  # Инкапсуляция
        self._fuel_consumption_loaded = fuel_consumption_loaded  # Инкапсуляция
        self.cargo_weight = cargo_weight  # Публичный атрибут

    def __str__(self) -> str:
        """Перегруженный метод для грузового автомобиля."""
        return f"Грузовик: {self._brand} {self._model} ({self._year} г.), грузоподъемность: {self._capacity} т"

    def __repr__(self) -> str:
        """Перегруженный метод для грузового автомобиля."""
        return (f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, "
                f"year={self._year}, capacity={self._capacity}, "
                f"fuel_consumption_empty={self._fuel_consumption_empty}, "
                f"fuel_consumption_loaded={self._fuel_consumption_loaded}, "
                f"mileage={self.mileage}, cargo_weight={self.cargo_weight})")

    def get_info(self) -> str:
        """
        Перегруженный метод для получения информации о грузовом автомобиле.

        Причина перегрузки: Необходимо добавить информацию о грузоподъемности и текущем грузе.

        Returns:
            str: Расширенная информация о грузовом автомобиле
        """
        base_info = super().get_info()
        return (f"{base_info}, грузоподъемность: {self._capacity} т, "
                f"текущий груз: {self.cargo_weight} т")

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Реализация абстрактного метода для расчета стоимости топлива.

        Args:
            distance: Расстояние в километрах
            fuel_price: Цена топлива за литр

        Returns:
            float: Стоимость топлива для поездки
        """
        # Выбираем расход в зависимости от наличия груза
        if self.cargo_weight > 0:
            fuel_consumption = self._fuel_consumption_loaded
        else:
            fuel_consumption = self._fuel_consumption_empty

        fuel_needed = (distance / 100) * fuel_consumption
        return round(fuel_needed * fuel_price, 2)

    def drive(self, distance: float) -> str:
        """
        Перегруженный метод для поездки на грузовом автомобиле.

        Причина перегрузки: Необходимо проверять, не превышен ли допустимый вес груза.

        Args:
            distance: Расстояние поездки в километрах

        Returns:
            str: Сообщение о поездке

        Raises:
            ValueError: Если вес груза превышает грузоподъемность
        """
        if self.cargo_weight > self._capacity:
            raise ValueError(
                f"Превышена грузоподъемность! Максимум: {self._capacity} т, текущий груз: {self.cargo_weight} т")

        # Используем метод родительского класса
        return super().drive(distance)

    def load_cargo(self, weight: float) -> str:
        """
        Унаследованный метод для загрузки груза.

        Args:
            weight: Вес груза для загрузки в тоннах

        Returns:
            str: Сообщение о загрузке

        Raises:
            ValueError: Если вес груза отрицательный или превышает грузоподъемность
        """
        if weight < 0:
            raise ValueError("Вес груза не может быть отрицательным")

        new_weight = self.cargo_weight + weight
        if new_weight > self._capacity:
            raise ValueError(f"Невозможно загрузить {weight} т. Превышение грузоподъемности!")

        self.cargo_weight = new_weight
        return f"Загружено {weight} т. Текущий груз: {self.cargo_weight} т"


if __name__ == "__main__":
    # Создаем экземпляры классов
    passenger_car = PassengerCar(
        brand="Toyota",
        model="Camry",
        year=2020,
        body_type="седан",
        fuel_consumption=8.5,
        mileage=15000,
        passenger_count=2
    )

    truck = Truck(
        brand="Volvo",
        model="FH",
        year=2019,
        capacity=20,
        fuel_consumption_empty=25,
        fuel_consumption_loaded=35,
        mileage=50000,
        cargo_weight=5
    )

    # Демонстрация работы методов
    print("=" * 50)
    print("БАЗОВЫЙ КЛАСС Vehicle (абстрактный, не создаем экземпляр)")
    print("=" * 50)

    print("\n" + "=" * 50)
    print("ЛЕГКОВОЙ АВТОМОБИЛЬ (PassengerCar)")
    print("=" * 50)
    print(f"__str__: {passenger_car}")
    print(f"__repr__: {repr(passenger_car)}")
    print(f"get_info(): {passenger_car.get_info()}")
    print(f"drive(100): {passenger_car.drive(100)}")
    print(f"add_passenger(): {passenger_car.add_passenger()}")
    print(f"calculate_fuel_cost(200, 50): {passenger_car.calculate_fuel_cost(200, 50)} руб.")

    print("\n" + "=" * 50)
    print("ГРУЗОВОЙ АВТОМОБИЛЬ (Truck)")
    print("=" * 50)
    print(f"__str__: {truck}")
    print(f"__repr__: {repr(truck)}")
    print(f"get_info(): {truck.get_info()}")
    print(f"drive(150): {truck.drive(150)}")
    print(f"load_cargo(10): {truck.load_cargo(10)}")
    print(f"calculate_fuel_cost(300, 55): {truck.calculate_fuel_cost(300, 55)} руб.")

    # Демонстрация обработки ошибок
    print("\n" + "=" * 50)
    print("ПРОВЕРКА ОБРАБОТКИ ОШИБОК")
    print("=" * 50)
    try:
        truck.load_cargo(10)  # Пытаемся загрузить слишком много
    except ValueError as e:
        print(f"Ошибка: {e}")

class Book:
    """Базовый класс для всех книг."""

    def __init__(self, name: str, author: str):
        """
        Инициализирует книгу.

        Args:
            name: название книги
            author: автор книги
        """
        self.name = name
        self.author = author

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """Возвращает валидную строку для инициализации такого же экземпляра."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажных книг, наследующийся от Book."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализирует бумажную книгу.

        Args:
            name: название книги
            author: автор книги
            pages: количество страниц
        """
        # Вызываем конструктор родительского класса
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        """Возвращает строковое представление бумажной книги."""
        # Можно использовать родительский __str__ или переопределить
        return f"{super().__str__()} - {self.pages} стр."

    def __repr__(self):
        """Возвращает валидную строку для инициализации такого же экземпляра."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс для аудиокниг, наследующийся от Book."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализирует аудиокнигу.

        Args:
            name: название книги
            author: автор книги
            duration: длительность в часах
        """
        # Вызываем конструктор родительского класса
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        """Возвращает строковое представление аудиокниги."""
        return f"{super().__str__()} - {self.duration} ч."

    def __repr__(self):
        """Возвращает валидную строку для инициализации такого же экземпляра."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == "__main__":
    # Создаем экземпляры разных типов книг
    book = Book("Война и мир", "Лев Толстой")
    paper_book = PaperBook("Преступление и наказание", "Федор Достоевский", 672)
    audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 16.5)

    # Проверяем методы __str__
    print(book)
    print(paper_book)
    print(audio_book)

    # Проверяем методы __repr__
    print(repr(book))
    print(repr(paper_book))
    print(repr(audio_book))

    # Проверяем атрибуты
    print(f"\nБумажная книга: {paper_book.name}, автор: {paper_book.author}, страниц: {paper_book.pages}")
    print(f"Аудиокнига: {audio_book.name}, автор: {audio_book.author}, длительность: {audio_book.duration} ч.")

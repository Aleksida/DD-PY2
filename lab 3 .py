class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self._author = author
        if not isinstance(name, str):
            raise TypeError("Имя автора должно быть типа str")

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name, author, pages: int):
        super().__init__(name, author)
        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно соответствовать типу int")
        if not pages > 0:
            raise ValueError("Количество страниц должно быть положительным")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
        if not isinstance(duration, float):
            raise TypeError('значение duration должно соответствовать типу float')
        if not duration > 0:
            raise ValueError("значение duration должно быть положительным")


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}'
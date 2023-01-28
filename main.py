# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Instagram:
    def __init__(self, seen_pics_quantity: int, likes_quantity: int, seen_stories_quantity: int):
        """
                Создание и подготовка к работе объекта "Инстаграм"
                :param seen_pics_quantity: Количество просмотренных публикаций
                :param slikes_quantity: Количество поставленных лайков
                :param seen_stories_quantity: Количество просмотренных историй
                Примеры:
                >>> instagram = Instagram(5,3,9)  # инициализация экземпляра класса
                """
        self.seen_pics_quantity = seen_pics_quantity
        self.likes_quantity = likes_quantity
        self.seen_stories_quantity = seen_stories_quantity
        if not isinstance(seen_pics_quantity, int):
            raise TypeError("Количество просмотренных публикаций должно быть типа int")
        if not seen_pics_quantity < 0:
            raise ValueError("Количество просмотренных публикаций должно быть положительным числом")
        if not isinstance(likes_quantity, int):
            raise TypeError("Количество лайков должно быть типа int")
        if not likes_quantity < 0:
            raise ValueError("Количество лайков должно быть положительным числом")
        if not isinstance(seen_stories_quantity, int):
            raise TypeError("Количество просмотренных историй должно быть типа int")
        if not seen_stories_quantity < 0:
            raise ValueError("Количество просмотренных историй должно быть положительным числом")

    def like_a_photo(self, more_likes:int) -> None:
        """
                Функция которая ставит лайки
                :return: Поставить лайк
                Примеры:
                >>> instagram = Instagram(5,3,9)
                >>> instagram.like_a_photo(1)
                """
        ...

    def see_a_story (self, more_stories) -> None:
        """
                        Функция которая просматривает истории
                        :return: Посмотреть историю
                        Примеры:
                        >>> instagram = Instagram(5,3,9)
                        >>> instagram.see_a_story(2)
                        """

    ...


class Music:
    def __init__(self, albums: int, playlists: int, tracks: int):
        """
                Создание и подготовка к работе объекта "Музыка"
                :param albums: Количество прослушанных альбомов
                :param playlists Количество прослушанных плейлистов
                :param tracks: Количество прослушанных треков
                Примеры:
                    >>> music = Music(5, 20, 211)  # инициализация экземпляра класса
        """
        self.albums = albums
        self.playlists = playlists
        self.tracks = tracks
        if not isinstance(albums, int):
            raise TypeError("Количество добавленных альбомов должно быть типа int")
        if not albums < 0:
            raise ValueError("Количество добавленных альбомов должно быть положительным числом")
        if not isinstance(playlists, int):
            raise TypeError("Количество добавленных плейлистов должно быть типа int")
        if not playlists < 0:
            raise ValueError("Количество добавленных плейлистов должно быть положительным числом")
        if not isinstance(tracks, int):
            raise TypeError("Количество добавленных треков должно быть типа int")
        if not tracks < 0:
            raise ValueError("Количество добавленных треков должно быть положительным числом")

    def add_a_track (self, more_tracks:int):
        """
            Добавление трека.
            :param more_tracks: количество добавляемых треков
            Примеры:
            >>>music = Music(5,10,20)
            >>>music.add_a_track(3)
        """
        if not isinstance(more_tracks, int):
            raise TypeError("Количество добавляемых треков должно быть типа int или float")
        if more_tracks < 0:
            raise ValueError("Количество добавляемых треков должно быть  положительным числом")
        ...

    def listen_to_playlist (self, more_playlists) -> None:
        """
            Прослушивание плейлиста.
            :param more_playlists: Количество новых прослушанных плейлистов.
            Примеры:
            >>> music = Music(5,10,20)
            >>> music.listen_to_playlist(3)
        """
        if not isinstance(more_playlists, int):
            raise TypeError("Количество новых прослушанных плейлистов должно быть типа int")
        if more_playlists < 0:
            raise ValueError("Количество новых прослушанных плейлистов должно быть  положительным числом")
        ...


class Candle:
    def __init__(self, candle_name: str, candles_quantity: int, candle_size: int):
        """
                Создание и подготовка к работе объекта "Свеча"
                :param candle_name: Название свечи
                :param candles_quantity: Количество свечей в наличии
                :param candle_size: Объём свечи в см квадратных
                Примеры:
                >>> candle = Candle(Orange, 5, 25)  # инициализация экземпляра класса
        """
        self.candle_name = candle_name
        self.candles_quantity = candles_quantity
        self.seen_stories_quantity = seen_stories_quantity
        if not isinstance(candle_name, str):
            raise TypeError("Название свечи должно быть типа str")
        if not isinstance(candles_quantity, int):
            raise TypeError("Количество свечей в наличии должно быть типа int")
        if not candles_quantity < 0:
            raise ValueError("Количество свечей в наличии должно быть положительным числом")
        if not isinstance(candle_size, int):
            raise TypeError("Объём свечи должен быть типа int")
        if not candle_size < 0:
            raise ValueError("Объём свечи должен быть положительным числом")

    def buy_a_candle(self, more_candles:int, candle_name: str) -> None:
        """
                    Покупка свечи.
                    :param more_candles: Количество новых свечей.
                    :param candle_name: Название покупаемой свечи.
                    Примеры:
                    >>> candle = Candle(Orange, 5, 25)
                    >>> candle.buy_a_candle(3, Orange)
        """

        if not isinstance(more_candles, int):
            raise TypeError("Количество новых свечей должно быть типа int")
        if more_candles < 0:
            raise ValueError("Количество новых свечей должно быть  положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


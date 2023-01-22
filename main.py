# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Instagram:
    def __init__(self, seen_pics_quantity: int, likes_quantity: int, seen_stories_quantity: int):
        self.seen_pics_quantity = seen_pics_quantity
        self.likes_quantity = likes_quantity
        self.seen_stories_quantity = seen_stories_quantity
        if not isinstance(seen_pics_quantity, int):
            raise TypeError("должен быть типа int")
        if not seen_pics_quantity < 0:
            raise ValueError("должен быть положительным числом")
        if not isinstance(likes_quantity, int):
            raise TypeError("должен быть типа int")
        if not likes_quantity < 0:
            raise ValueError("должен быть положительным числом")
        if not isinstance(seen_stories_quantity, int):
            raise TypeError("должно быть типа int")
        if not seen_stories_quantity < 0:
            raise ValueError("должно быть положительным числом")

def like_a_photo(self, more_likes:int) -> None:
    self.likes_quantity += more_likes

def see_a_story (self, more_stories) -> None:
    self.seen_stories_quantity += more_stories

if __name__ == "__main__":
    doctest.testmod()    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class Music:
    def __init__(self, albums: int, playlists: int, tracks: int):
        self.albums = albums
        self.playlists = playlists
        self.tracks = tracks
        if not isinstance(albums, int):
            raise TypeError("должен быть типа int")
        if not albums < 0:
            raise ValueError("должен быть положительным числом")
        if not isinstance(playlists, int):
            raise TypeError("должен быть типа int")
        if not playlists < 0:
            raise ValueError("должен быть положительным числом")
        if not isinstance(tracks, int):
            raise TypeError("должно быть типа int")
        if not tracks < 0:
            raise ValueError("должно быть положительным числом")

def add_a_track (self, more_tracks:int):
    self.tracks += more_tracks
    if tracks < 10:
        raise ValueError ("Количество добавленных треков должно быть не меньше 10")

def listen_to_playlist (self, more_playlists) -> None:
    self.playlists += more_playlists

if __name__ == "__main__":
    doctest.testmod()    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
class Candle:
    def __init__(self, candle_name: str, candles_quantity: int, candle_size: int):
        self.candle_name = candle_name
        self.candles_quantity = candles_quantity
        self.seen_stories_quantity = seen_stories_quantity
        if not isinstance(candle_name, str):
            raise TypeError("должен быть типа str")
        if not isinstance(candles_quantity, int):
            raise TypeError("должен быть типа int")
        if not candles_quantity < 0:
            raise ValueError("должен быть положительным числом")
        if not isinstance(candle_size, int):
            raise TypeError("должно быть типа int")
        if not candle_size < 0:
            raise ValueError("должно быть положительным числом")

def buy_a_candle(self, more_candles:int) -> None:
    self.candles_quantity += more_candles

def choose_candle (self, candle_name:str):
#Выбор свечки
        #:raise ValueError: Если свеча не типа str)
        #Примеры:
        #>>> Candle = Candle(Vanilla, 1, 30)
        #>>> Candle.choose_candle(vanilla)

        if not isinstance(candle_name, str):
            raise TypeError("Вид свечи должен быть типа str")
        ...

if __name__ == "__main__":
    doctest.testmod()    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


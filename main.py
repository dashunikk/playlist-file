## project_7

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * кортеж строк
#   * словарь
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

import random
from datetime import timedelta
from typing import Iterable, Any

playlist_c = (
	"Happy Nation; 3.32",
	"It's My Life; 3.59",
	"Lady(Hear Me Tonight); 5.07",
	"Fields Of Gold; 3.38",
	"The Winner Takes It All; 4.54",
	"Self Control; 4.06",
	"I Shot The Sheriff; 4.57",
	"Don't Give Up; 6.34",
	"Relax, Take It Easy; 4.30",
	"Dancing Queen; 3.36",
)

playlist_b = {
	'Портофино': 3.32,
	'Снег': 4.35,
	'Попытка №5': 3.23,
	'Тополиный Пух': 3.53,
	'Если хочешь остаться': 4.48,
	'Зеленоглазое такси': 5.52,
	'Ты не верь слезам': 3.1,
	'Nowhere to Run': 2.58,
	'Салют, Вера': 4.44,
	'Улетаю': 3.24,
	'Опять метель': 3.37,
	}

# даёт рандомные песни из двух плейлистов (теперь может работать и с кортежами, и со словарями)
def get_random_songs(playlist: Iterable, n: int) -> list:
    if isinstance(playlist, dict):
        songs = list(playlist.items())
    else:
        songs = list(playlist)

    random.shuffle(songs)
    return songs[:n]

# штука, которая заберет время из песен (работает и с : и с ;)
def extract_duration(song: Any) -> float:
    if isinstance(song, tuple):
        duration_str = song[1]
    elif isinstance(song, str):
        duration_str = song.split(';')[-1].strip()

# Проверка (float или int)
    if isinstance(duration_str, (float, int)):
        minutes = int(duration_str)
        seconds = (duration_str - minutes) * 100
        return minutes * 60 + int(seconds)
    
def get_total_duration(playlist: Iterable, n: int) -> Any:
    """
    Выбирает n случайных песен из плейлиста,
    вычисляет их общую длительность и возвращает в формате timedelta.
    """
    # Выбираем n случайных песен
    selected_songs = random.sample(playlist, n)
    
    # Преобразуем длительности песен в секунды и суммируем
    total_duration_seconds = sum(
        int(duration.split('.')[0]) * 60 + int(duration.split('.')[1])
        for duration in selected_songs
    )
    
    # Возвращаем результат в формате timedelta
    return timedelta(seconds=total_duration_seconds)

def print_total_duration(playlist_name, playlist):
    total_time = get_duration(playlist, 1)
    print(f"Общее время звучания ({playlist_name}): {total_time}")

# Вычисляем и выводим общее время звучания для каждого плейлиста
print_total_duration("playlist_c", playlist_c)
print_total_duration("playlist_b", playlist_b)
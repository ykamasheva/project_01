# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
from pprint import pprint
import random
from random import sample
songs = list(my_favorite_songs.items())
random_songs = sample(songs,3)
print (random_songs)
print ('Три песни звучат', random_songs[0][1]+random_songs[1][1]+random_songs[2][1], 'минут')

#!/usr/bin/env python

# В. Пупкин развозит пиццу. Ему сообщают адрес доствки в виде
# <улица> <номер дома>-<номер квартиры>
#
# Приезжая по указанному адресу, Вася видит f-этажное здание.
# Для простоты будем считать, что на каждом этаже в подъезде находятся 4 квартиры.
#
# Помогите Васе посчитать, в каком подъезде и на каком этаже находится нужная квартира n.
#
# Для решения понадобится использовать деление по модулю %
# или целочисленное деление //.
from math import *

num_f = 4
'''Кол-во квартир на одном этаже'''


def find_flats(home_high):
    """
    home_high - число этажей в доме
    num_kv - номер квартиры
    """
    return num_f * home_high


def find_entrance(home_high, num_kv):
    """
    home_high - число этажей в доме
    num_kv - номер квартиры
    """
    return ceil(num_kv / find_flats(home_high))


def find_floor(home_high, num_kv):
    """
    home_high - число этажей в доме
    num_kv - номер квартиры
    """
    num_kv_entr = num_kv % find_flats(home_high)
    if num_kv_entr == 0:
        return home_high
    else:
        return ceil(num_kv_entr / num_f)


if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    flat_num = int(input("Номер квартиры: "))

    entrance = find_entrance(floors, flat_num)
    floor = find_floor(floors, flat_num)
    print(entrance, floor)

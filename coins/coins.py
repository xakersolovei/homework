#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:
    minimum = min(a, b, c)
    summa = (a + b + c) - minimum
    return summa

if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("a = "))
    c = int(input("a = "))

    print(max_sum_of_2(a, b, c))

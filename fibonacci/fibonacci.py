#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""
import math

cv = math.sqrt(5)

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be >= 0")

    return int(((cv + 1) / 2) ** n / cv + 0.5)

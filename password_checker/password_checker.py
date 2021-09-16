#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации
"""
import string


def is_strong_password(pwd: str) -> bool:
    answer = False

    if len(pwd) >= 10:
        lower = False
        upper = False
        digit = False
        punctuation = False

        for i in range(len(pwd)):

            if pwd[i] in string.ascii_lowercase:
                lower += 1
                continue

            if pwd[i] in string.ascii_uppercase:
                upper += 1
                continue

            if pwd[i] in string.digits:
                digit += 1
                continue

            if pwd[i] in string.punctuation:
                punctuation += 1

        answer = lower > 0 and upper > 0 and digit > 0 and punctuation > 0

    return answer

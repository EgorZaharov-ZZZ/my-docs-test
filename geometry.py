"""
Модуль для расчёта площади фигур.
"""

def calculate_area(radius: float) -> float:
    """
    Вычисляет площадь круга.

    :param radius: Радиус круга (положительное число).
    :return: Площадь круга (число).
    """
    import math
    return math.pi * radius ** 2

def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Вычисляет площадь прямоугольника.

    :param length: Длина прямоугольника (положительное число).
    :param width: Ширина прямоугольника (положительное число).
    :return: Площадь прямоугольника (число).
    """
    return length * width
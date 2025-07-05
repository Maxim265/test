import math

def get_positive_integer():
    """Запрашивает у пользователя положительное целое число и возвращает его.
    Обрабатывает возможные ошибки ввода.
    """
    while True:
        try:
            number = int(input("Введите положительное целое число: "))
            if number < 0:
                raise ValueError("Число должно быть положительным.")
            return number
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте еще раз.")

def calculate_factorial(n):
    """Вычисляет факториал числа n с использованием библиотеки math."""
    return math.factorial(n)

def main():
    """Основная функция программы."""
    number = get_positive_integer()
    factorial = calculate_factorial(number)
    print(f"Факториал числа {number} равен {factorial}.")

if __name__ == "__main__":
    main()

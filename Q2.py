import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    print("Угадайте число от 1 до 100. У вас есть 10 попыток.")

    for attempt in range(attempts):
        guess = int(input(f"Попытка {attempt + 1}: Ваше предположение: "))

        if guess < number_to_guess:
            print("Слишком маленькое число!")
        elif guess > number_to_guess:
            print("Слишком большое число!")
        else:
            print("Вы угадали число!")
            break

    else:
        print(f"Попытки закончились, загаданное число было {number_to_guess}.")

guess_the_number()
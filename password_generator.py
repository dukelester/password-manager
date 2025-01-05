import string
import random


def password_generator(nr_letters=15, nr_symbols=3, nr_numbers=4):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    numbers = string.digits         # Contains 0-9
    symbols = "!#$%&()*+"

    # Generate password components
    letter_choice = random.choices(letters, k=nr_letters)
    symbols_choice = random.choices(symbols, k=nr_symbols)
    number_choice = random.choices(numbers, k=nr_numbers)

    # Combine and shuffle
    password_list = letter_choice + symbols_choice + number_choice
    random.shuffle(password_list)

    return "".join(password_list)


# Example usage
print(password_generator())


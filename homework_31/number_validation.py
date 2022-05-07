def number_validation(first_number, second_number):
    if first_number.isdigit() and second_number.isdigit():
        return int(first_number), int(second_number)
    elif float(first_number) and float(second_number):
        return float(first_number) and float(second_number)
    else:
        return False


def numbers():
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    return first_number, second_number
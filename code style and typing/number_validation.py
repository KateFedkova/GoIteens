from typing import Any, Union, Tuple


def number_validation(first_number: Any,
                      second_number: Any) -> \
        Union[Tuple[float, float], bool]:
    '''Check if all numbers are digits'''
    if first_number.replace('.', '').isdigit and second_number.replace('.', '').isdigit():
      return first_number, second_number
    return False

def numbers() -> Any:
    '''Input numbers'''
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    return first_number, second_number
  

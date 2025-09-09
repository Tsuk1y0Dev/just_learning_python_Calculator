class CalculatorError(Exception):
    """Базовое исключение для ошибок калькулятора."""
    pass

class DivisionByZeroError(CalculatorError):
    """Исключение для деления на ноль."""
    pass

class InvalidOperationError(CalculatorError):
    """Исключение для недопустимых операций."""
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError("Деление на ноль невозможно")
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        raise DivisionByZeroError("Деление на ноль невозможно")
    return a % b

def calculate(operation, a, b):

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        '%': modulus
    }
    
    if operation not in operations:
        raise InvalidOperationError(f"Неподдерживаемая операция: {operation}")
    
    return operations[operation](a, b)

if __name__ == "__main__":
    # Тестирование функций при прямом запуске модуля
    try:
        result = calculate('+', 5, 3)
        print(f"5 + 3 = {result}")
        
        result = calculate('/', 10, 0)
        print(f"10 / 0 = {result}")
        
    except CalculatorError as e:
        print(f"Ошибка калькулятора: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Тестирование завершено")
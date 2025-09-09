from utils import calculate, CalculatorError, DivisionByZeroError, InvalidOperationError

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите число")

def main():
    """Основная функция калькулятора."""
    print("Поддерживаемые операции: +, -, *, /, ^ (степень), % (остаток от деления)")

    try:
        # Получаем операцию
        operation = input("Введите операцию: ").strip()
        
        # Получаем числа
        a = get_number_input("Введите первое число: ")
        b = get_number_input("Введите второе число: ")
        
        # Выполняем вычисление
        result = calculate(operation, a, b)
        
        # Выводим результат
        print(f"Результат: {result}")
        
    except DivisionByZeroError as e:
        print(f"Математическая ошибка: {e}")
    except InvalidOperationError as e:
        print(f"Ошибка операции: {e}")
    except CalculatorError as e:
        print(f"Ошибка калькулятора: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    else:
        print("Вычисление выполнено успешно!")
    finally:
        print("Спасибо за использование калькулятора!")

if __name__ == "__main__":
    main()

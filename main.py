# ==============================
#       КАЛЬКУЛЯТОР v2.0
# ==============================

history = []


def format_number(num):
    """Убирает .0 у целых чисел"""
    if num == int(num):
        return int(num)
    return num


print("===================================")
print("      Добро пожаловать!")
print("         КАЛЬКУЛЯТОР")
print("===================================")

while True:

    # Ввод первого числа
    while True:
        try:
            a = float(input("\nВведите первое число: "))
            break
        except:
            print("Ошибка! Введите число.")

    # Ввод второго числа
    while True:
        try:
            b = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    # Выбор операции
    while True:
        operation = input("Введите операцию (+, -, *, /): ")

        if operation in ["+", "-", "*", "/"]:
            break

        print("Такой операции не существует!")

    # Выполнение вычислений
    if operation == "+":
        result = a + b

    elif operation == "-":
        result = a - b

    elif operation == "*":
        result = a * b

    else:
        if b == 0:
            print("Ошибка! Деление на ноль невозможно.")
            continue
        result = a / b

    # Красивый вывод
    a = format_number(a)
    b = format_number(b)
    result = format_number(result)

    expression = f"{a} {operation} {b} = {result}"

    print("\nРезультат:")
    print(expression)

    history.append(expression)

    # Меню
    print("\n-----------------------------")
    print("1 - Новое вычисление")
    print("2 - История вычислений")
    print("3 - Очистить историю")
    print("4 - Выход")
    print("-----------------------------")

    choice = input("Выберите действие: ")

    if choice == "1":
        continue

    elif choice == "2":
        if len(history) == 0:
            print("История пуста.")
        else:
            print("\nИстория вычислений:")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")

    elif choice == "3":
        history.clear()
        print("История очищена.")

    elif choice == "4":
        print("\nСпасибо за использование калькулятора!")
        break

    else:
        print("Неизвестная команда.")
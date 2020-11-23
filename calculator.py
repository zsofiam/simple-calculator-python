def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_valid_operator(operator):
    operator_list = ["+", "-", "*", "/"]
    if operator in operator_list:
        return True
    else:
        return False


def ask_for_a_number(force_valid_input):
    while True:
        user_input = input("Please provide a number!")
        if is_number(user_input):
            return float(user_input)
        else:
            if not force_valid_input:
                return None
            print("This didn't look like a number, try again.")


def ask_for_an_operator(force_valid_input):
    while True:
        user_input = input("Please provide an operator (one of +,-,*,/)!")
        if is_valid_operator(user_input):
            return user_input
        else:
            if not force_valid_input:
                return None
            print("Unknown operation.")


def calc(operator, a, b):
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    result = None
    if(operator == "+"):
        result = a + b
    elif(operator == "-"):
        result = a - b
    elif(operator == "*"):
        result = a * b
    elif(operator == "/"):
        try:
            a / b
        except ZeroDivisionError:
            result = None
            print("Error: Division by zero") 
        else:
            result = a / b
    return result


def simple_calculator():
    while True:
        number1 = ask_for_a_number(force_valid_input=False)
        if not number1:
            break
        operator = ask_for_an_operator(True)
        number2 = ask_for_a_number(True)
        result = calc(operator, number1, number2)
        print("The result is " + str(result) + ".")


if __name__ == '__main__':
    simple_calculator()


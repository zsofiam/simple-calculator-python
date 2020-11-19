# Simple Calculator

## Story

Your task is to implement a simple calculator script ask the user
to enter a number, then an operation (like `+` and `/`), then a
number again. After the 2nd number input, the result of the
operation should be calculated and printed out. Then the program
should start asking again for a first number.

The script should exit when the user enters a non-numeric
expression (like a letter) _for the first number_ input.

!> This is a **guided project**, a regular project with a step-by-step guide
   (see the Background materials). In order to learn the most, try and
   implement it on your own first, and check the solution only when you feel
   your version is ready. However, when you feel completely stuck, feel free
   to check the guide for hints.

## What are you going to learn?

- more advanced conditional statements
- type conversion
- basic exception handling

## Tasks

1. Implement `is_number(str)` to return the numeric value of the string `str` if possible, otherwise return `None`
    - The checker works for strings representing non-negative integers.
    - The checker works for strings representing any integers.
    - The checker works for strings representing any numbers.
    - The checker returns either a number or `None`, and never raises an exception

2. Implement `is_valid_operator(operator)` to return with `True` if the `operator` input parameter represents a valid operator, otherwise return with `False`.
    - Valid operators are the following&#58; +, -, *, /.

3. Implement `ask_for_a_number(force_valid_input)` to return the numeric value of the user input. The function continuously ask an input from the user while it is not numeric when `force_valid_input` is `True`. When the `force_valid_input` is `False` and the user input is not numeric, the function returns with `None`.
    - The function asks an input from the user, e.g.&#58; 'Please provide a number! '.
    - The function returns with the numeric value of the input string if it represents a valid number.
    - The function returns with `None` when the user input not represents any number and `force_valid_input` is `False`.
    - In case of `force_valid_input` is `True`, the function continuously ask for a number, while the provided input string not represents a valid number. After an unsuccessful input, the program inform the user about the wrong input, e.g.&#58; 'This didn't look like a number, try again.'.

4. Implement `ask_for_an_operator(force_valid_input)` to return with a valid operator. The function continuously ask an operator from the user while it is not valid operator when `force_valid_input` is `True`. When the `force_valid_input` is `False` and the user input is not a valid operator, the function returns with `None`.
    - The function asks an input from the user, e.g.&#58; 'Please provide an operator (one of +, -, *, /)! '.
    - The function returns with an operator if the input string represents a valid operator.
    - The function returns with `None` when the user input not represents valid operator and `force_valid_input` is `False`.
    - In case of `force_valid_input` is `True`, the function continuously ask for an operator, while the provided input string not represents a valid operator. After an unsuccessful input, the program inform the user about the wrong input, e.g.&#58; 'Unknown operator.'.

5. Implement `calc(operator, a, b)` to calculate the result of the 'a' 'operator' 'b' operator. The function returns with `None` if any operand or the operator is not valid. The function handles division by zero, in this case the return value is `None`
    - The function checks the validity of the operands and the operator. Returns with `None` in case of any invalid input.
    - The function returns with the result of 'a' + 'b' if the operator is '+'.
    - The function returns with the result of 'a' - 'b' if the operator is '-'.
    - The function returns with the result of 'a' \* 'b' if the operator is '\*'.
    - The function returns with the result of 'a' / 'b' if the operator is '/' and b is not equal to 0. If the 'b' is equal to 0, the function prints an error message, e.g.&#58; 'Error&#58; Division by zero' and returns with `None`.

6. Implement `simple_calculator()` to create the calculator. The function continuously asks for number 'a' and 'b' and an operator and calculates the result of 'a' 'operator' 'b'.
    - The function checks the validity of the operands and the operator. Exit from the program if the 'a' operand is not valid. In case of valid 'a' operand, the function ensures the operand 'b' and the operator is valid.
    - The function prints the calculation results, e.g.&#58; 'The result is 10'.

## General requirements

None

## Hints

- You need a function for asking input number from the user. For the first number request, non-number input is acceptable (this will trigger the exit from the program), but for the second input request is not allowed. You can distinguishes between the two case with a boolean variable.
- Create a helper function called input, which will contain the Scanner. It is a good idea to outsource all functionality that is used more than once.

## Starting your project



## Background materials

- <i class="far fa-exclamation"></i> [Control structures](project/curriculum/materials/pages/python/control-structures.md)
- <i class="far fa-exclamation"></i> [Error handling and exceptions](project/curriculum/materials/pages/python/error-handling-and-exceptions-debugging-logging.md)
- <i class="far fa-exclamation"></i> [Getting user input](project/curriculum/materials/pages/python/user-input.md)
- <i class="far fa-exclamation"></i> [Top-level script environment](https://docs.python.org/3/library/__main__.html)
- <i class="far fa-candy-cane"></i> [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
- <i class="far fa-candy-cane"></i> [Python "while" Loops](https://realpython.com/python-while-loop/)
- <i class="far fa-candy-cane"></i> [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [A step-by-step solution guide](project/curriculum/materials/pages/python/simple-calculator-step-by-step.md)


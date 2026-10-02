# Factorial using recursion
def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
print(factorial(0), factorial(1))


# Seeing recursive calls
def show_factorial(number, level=0):
    spaces = " " * level
    print(f"{spaces}factorial({number})")

    if number <= 1:
        print(f"{spaces}-> returns 1")
        return 1

    answer = number * show_factorial(number - 1, level + 1)

    print(f"{spaces}-> returns {answer}")
    return answer


show_factorial(4)


# Countdown without a stopping condition
def count_down(number):
    print(number)
    count_down(number - 1)


# This would continue forever, so don't call it.


# Countdown with a base case
def launch_countdown(number):
    if number <= 0:
        print("Liftoff!")
        return

    print(number)
    launch_countdown(number - 1)


launch_countdown(3)


# Fibonacci series
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


for number in range(8):
    print(fibonacci(number), end=" ")

print()


# Comparing loop and recursion
def factorial_using_loop(number):
    answer = 1

    for value in range(2, number + 1):
        answer *= value

    return answer


def factorial_using_recursion(number):
    if number <= 1:
        return 1

    return number * factorial_using_recursion(number - 1)


print(factorial_using_loop(5))
print(factorial_using_recursion(5))
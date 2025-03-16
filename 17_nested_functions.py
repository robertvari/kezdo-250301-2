def calculate_result(num1, num2):
    def add_numbers(a, b):
        return a+b

    def divide_numbers(a, b):
        return a/b

    def multiply_numbers(a,b):
        return a*b

    add_result = add_numbers(num1, num2)
    divide_result = divide_numbers(add_result, num2)
    multiply_result = multiply_numbers(divide_result, num2)

    return multiply_result



result = calculate_result(10, 5)
print(result)
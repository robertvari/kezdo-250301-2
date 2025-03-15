def recursive_function(number):
    number += 1
    print(f"Number: {number}")

    # stop recursion when number == 10
    if number == 10:
        return

    recursive_function(number)


recursive_function(0)
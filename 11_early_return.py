def early_return(number: int):
    if number > 10:
        # early return
        return "The number is greater than 10"
    
    return number

result = early_return( input("Give me a number") )
print(result)
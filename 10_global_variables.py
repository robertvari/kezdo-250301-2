NAME = "Tamás"

def say_hello():
    global NAME
    NAME = "Csaba"

def change_name(name):
    global NAME
    NAME = name

say_hello()
print(NAME)
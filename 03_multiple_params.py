def say_hello(email, name, address):
    print(f"Hello {name}")
    print(f"You live in {address}")
    print(f"Your email is {email}")

# posittional arguments/parameters
say_hello("Csaba", "Budapest", "csaba@gmail.com")

# keyword params
say_hello(email="csaba@gmail.com", name="Csaba", address="Budapest")
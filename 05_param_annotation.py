def say_hello(name: str, age: int, address: str):
    assert isinstance(name, str), "name must be of type string"
    assert isinstance(age, int), "age must be of type int"
    assert isinstance(address, str), "address must be of type string"


say_hello("Robert", 22, "Budapest")
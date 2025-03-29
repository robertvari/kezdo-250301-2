def args_test(*args):
    print(args)

def qwargs_test(**kwargs):
    print(kwargs)

def args_qwargs_test(*args, **qwargs):
    print(args)
    print(qwargs)

args_test("Tamás", 10, "Budapest", 3.14)
qwargs_test(
    email="csaba@gmail.com",
    name="Csaba",
    address="Budapest"
)

args_qwargs_test(
    "Tamás", 10, "Budapest", 3.14,
    email="csaba@gmail.com",
    name="Csaba",
    address="Budapest"
)
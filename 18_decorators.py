import time, random
from my_functions.decorators import my_timer

def useles_decorator(func):
    def wrapper(*args, **quargs):
        print("Hello! I'm not even here :PPP")
        result = func(*args, **quargs)
        return result
    return wrapper

@my_timer
@useles_decorator
def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished.")

@my_timer
def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished.")

@my_timer
def worker3():
    print("Worker 3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished.")


worker1()
worker2()
worker3()
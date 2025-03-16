import time, random

def my_timer(func):

    def wrapper(*args, **qwargs):
        start_time = time.time()
        result = func(*args, **qwargs)
        stop_time = time.time()
        print(f"Process time: {stop_time-start_time}")
        return result
    
    return wrapper

def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished.")

def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished.")

def worker3():
    print("Worker 3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished.")


worker1()
worker2()
worker3()
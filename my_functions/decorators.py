import time

def my_timer(func):
    def wrapper(*args, **qwargs):
        start_time = time.time()
        result = func(*args, **qwargs)
        stop_time = time.time()
        print(f"Process time: {stop_time-start_time}")
        return result
    
    return wrapper
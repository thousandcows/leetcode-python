import time


def time_measurement(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nExecution Time: {execution_time:.9f} seconds")
        return result

    return wrapper

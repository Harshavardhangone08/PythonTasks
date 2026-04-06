'''
Performance Tracker (Decorators)
A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function.
'''
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end-start:.6f}")
    return wrapper
@timer
def test():
    for i in range(1000000):
        pass
test()
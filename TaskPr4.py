import time
from functools import wraps

def timer_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {execution_time:.6f} секунд")
        return result
    return wrapper

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci_seq_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

@timer_wrapper
def prime_num_getter(n):
    generator = fibonacci_seq_generator()
    prime_numbers = []
    for _ in range(n):
        prime_number = next(generator)
        prime_numbers.append(prime_number)
    print(f"Перші {n} простих чисел: {prime_numbers}")
    return prime_numbers

if __name__ == "__main__":
    prime_num_getter(10)
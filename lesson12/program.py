import time

"""
start_time = time.time()
result = method(*args)
end_time = time.time()
print(f"Time taken: {method.__name__}: {end_time - start_time:.4f} sec")"""
def timer_decorator(method):
        def wrapper(*args):
            start_time = time.time()
            result = method(*args)
            end_time = time.time()
            print(f"Time taken: {method.__name__}: {end_time - start_time} sec")
            return result

        return wrapper

def repeater_decorator(n):
    def repeat_n_times_decorator(method):
        def wrapper(*args):
            for i in range(n):
                result = method(*args)
            return result
        return wrapper
    return repeat_n_times_decorator

counter = {}
def count_func_repeat(method):
    def wrapper(*args):
        if method.__name__ in counter:
            counter[method.__name__] += 1
        else:
            counter[method.__name__] = 1
        print(f"{method.__name__}: {counter[method.__name__]} times")
        return method(*args)
    return wrapper

class FileReader:
    @repeater_decorator(n=4)
    @count_func_repeat
    @timer_decorator
    def read_file(self,file):
        filer = ''
        with open(file,"r") as f:
            filer = f.read()
        return filer

fr = FileReader()
fr.read_file("some.txt")
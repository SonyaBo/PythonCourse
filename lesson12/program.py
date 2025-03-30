import time

counter = {}


def handler(default):
    def exception_handler(method):
        def wrapper(*args):
            try:
                return method(*args)
            except Exception:
                return default

        return wrapper

    return exception_handler


def timer_decorator(method):
    def wrapper(*args):
        start_time = time.time()
        result = method(*args)
        end_time = time.time()
        print(f"Time taken: {method.__name__}: {end_time - start_time} sec")
        return result

    return wrapper


def block_call(method):
    def wrapper(*args):
        if counter[method.__name__] >= 4:
            return "Limit of calls reached."
        else:
            return method(*args)
    return wrapper()


def repeater_decorator(n):
    def repeat_n_times_decorator(method):
        def wrapper(*args):
            for i in range(n):
                result = method(*args)
            return result

        return wrapper

    return repeat_n_times_decorator


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

    @count_func_repeat
    def read_file(self, file):
        filer = ''
        with open(file, "r") as f:
            filer = f.read()
        return filer


fr = FileReader()

fr.read_file()

fr.read_file()
fr.read_file()
fr.read_file()
print(counter)
print(fr.read_file())

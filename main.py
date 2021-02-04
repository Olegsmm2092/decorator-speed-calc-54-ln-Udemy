from time import *
# current_time = time.now() or just time()
current_time = time()

def delay_func(func): # or speed calc or speed checker or time checker how much time was look up foxford 1-2
    def wrapper():
#         do smth before
        begin_time = time()
        func()
        end_time = time()
        print(f"{func.__name__} run speed: {end_time - begin_time}s")
#         do smth after
        
    return wrapper

@delay_func
def fast_func():
    num = [n*n for n in range(10**6)]
    return num

@delay_func
def slow_func():
    num = [n*n for n in range(10**6)]
    return num


fast_func()
slow_func()
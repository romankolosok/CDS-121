import time

def time_decorator(func):
    def execution_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} function exrcution time is {(end_time - start_time):.3} seconds")
    return execution_time

@time_decorator
def calculate_odd(array):
    count = 0;
    for element in array:
        if element % 2:
            count += 1
    return count

calculate_odd(list(range(1,100000000)))


#Question 2
#I think we're only suppose to use them in variables which store some parameters from particular object, like __name__  for object <function>.
# Variables with __ are reserved in python, I think we can break something in object or at least error will be raised when we will try to change them.
# I'd rather avoid using __ in variable names not to get some unexpected results. Purpose of __variables__ is to get values of object'  s attributes





#I'm not sure whether I interpreted the condition correctly, I hope that solution below is what condition asked me to do :)
def filter(ch):
    def inner_function(string):
        if len(set(string)) == 1:
            return string.replace(ch, "*")
        raise ValueError(f"'{string}' string should consist from only one character")

    return inner_function

print(filter("s")("ssssss"))
# print(filter("a")("ssssss"))
# print(filter("s")("sdssss"))

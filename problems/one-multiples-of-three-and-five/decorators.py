import functools

def input_is_integer(value):
    def decorator_input_is_integer(func):
        @functools.wraps(func)
        def wrapper_input_is_integer(*args, **kwargs):
            try:
                return int(value)
            else:
                print("not an integer")
import functools
from enum import Enum
import os

type_conversion = {int: "int64", str: "str", list: "arr"}

def generate_action(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        if not os.path.exists("msg"):
            os.makedirs("msg")
        with open("msg/arg_msg.msg", "w") as f:
            for arg in args:
                f.write(type_conversion[type(arg)] + ' ' + str(arg) + '\n')
        ret_value = func(*args, **kwargs)
        # Do something after
        with open("msg/ret_msg.msg", "w") as f:
            f.write(type_conversion[type(ret_value)] + ' ' + str(ret_value) + '\n')

        if not os.path.exists("action"):
            os.makedirs("action")
        with open("action/action.action", "w") as f:
            f.write("int64 a\n---\nint64 b\n---\nint64 c")

        return ret_value
    return wrapper_decorator

@generate_action
def example_func(my_int: int, my_str: str, my_list: list) -> int:
    x = my_str
    y = my_list
    return my_int

example_func(4, "hi", [1,2,3])

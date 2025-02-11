def get_int():
    return 100

def get_float():
    return 89.91

def get_string():
    return "$tr!ng"

def get_bool():
    return True

def get_list():
    return [5, 44, 12]


# anything inside the curly braces is replaced by the value of the variable or function
print(f"Integer: {get_int()}")
print(f"Float: {get_float()}")
print(f"String: {get_string()}")
print(f"Boolean: {get_bool()}")
print(f"List: {get_list()}")

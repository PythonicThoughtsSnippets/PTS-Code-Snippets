# Python Thougts Snippets #1
# python 3.7
# 2019-08-15
# blog plost: https://viviendomochileros.com/2019/08/15/python-thoughts-snippets-control-flow-1/

# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE
# TO RAISE DISCUSSION

def translate_ifs(val):
    
    if isinstance(val, str):
        return val
    
    elif isinstance(val, int):
        return str(val)
    
    elif bool(val is False):
        return 'F'
    
    elif bool(val is True):
        return 'T'
    
    else:
        raise SomeError('My control Flow Error!')


# evaluates WITHOUT else statement
def translate_1(val):
    
    d = {
        isinstance(val, str): val,
        isinstance(val, int): str(val),
        bool(val is False): 'F',
        bool(val is True): 'T',
        }
    
    try:
        return d[True]
    except IndexError:
        pass  # handle exception here


# evaluates WITH else statement
def translate_2(val):
    
    d = {
        True: 'Happy Flowers!',
        isinstance(val, str): val,
        isinstance(val, int): str(val),
        bool(val is False): 'F',
        bool(val is True): 'T',
        }
    
    return d[True]


# Because functions in Pyhon are first class objects...
def translate_3(val):
    
    d = {
        True: func1,
        isinstance(val, str): func2,
        isinstance(val, int): func3,
        bool(val is False): func4,
        bool(val is True): func5,
        }
    
    return d[True](val)


# # you can even use partials to prepare function calls
def translate_4(val):
    
    from functools import partial
    
    d = {
        True: partial(func1, some_val),
        isinstance(val, str): partial(func2, some_val),
        isinstance(val, int): partial(func3, some_val),
        bool(val is False): partial(func4, some_val),
        bool(val is True): partial(func5, some_val),
        }
    
    return d[True]()

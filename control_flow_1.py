# python 3.7
# 2019-08-15

def val_to_trades_option_ifs(val):
    
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
def val_to_trades_option_1(val):
    
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
def val_to_trades_option_2(val):
    
    d = {
        True: 'Happy Flowers!',
        isinstance(val, str): val,
        isinstance(val, int): str(val),
        bool(val is False): 'F',
        bool(val is True): 'T',
        }
    
    return d[True]


# Because functions in Pyhon are first class objects...
def val_to_trades_option_3(val):
    
    d = {
        True: func1,
        isinstance(val, str): func2,
        isinstance(val, int): func3,
        bool(val is False): func4,
        bool(val is True): func5,
        }
    
    return d[True](val)


# # you can even use partials to prepare function calls
def val_to_trades_option_4(val):
    
    from functools import partial
    
    d = {
        True: partial(func1, some_val),
        isinstance(val, str): partial(func2, some_val),
        isinstance(val, int): partial(func3, some_val),
        bool(val is False): partial(func4, some_val),
        bool(val is True): partial(func5, some_val),
        }
    
    return d[True]()

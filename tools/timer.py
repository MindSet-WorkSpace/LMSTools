import time


def call_me_back(*args):
    """accepts and prints as when argument as possible"""
    print('Hello and welcome to Python\'s world oof programming')
    print('Welcome to the programming world, where we eat python (not the snake!!!) as food')
    print(args[1], args)


def the_timer(timer, callback=None, args=None):
    """the_timer(timer, callback) - argument timer contains the seconds you want the program to run and callback is the
    function you wish to callback."""
    if not callable(callback):
        raise NotImplementedError("'callback' is not a function")
    for i in range(timer):
        time.sleep(1)  # argument taken is equal to the number of seconds the execution can be delayed
        callback(i) if not args else callback(i, *args)


def digital_clock(callback=None):
    if not callable(callback):
        raise NotImplementedError("'callback' is not a function")
    while True:
        result = time.strftime('%I:%M:%S %p', time.localtime())
        callback(result)
        time.sleep(1)


if __name__ == '__main__':
    the_timer(10, call_me_back)
    digital_clock()

import functools


def outher_function(func):
    print(f'inner function {func}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper documentation

        """
        print('other some things done 1')

        return func(*args, **kwargs)

    return wrapper


@outher_function
def some_function_1(param):
    '''
    somehing....
    '''
    # print(param+1)
    print(f'some function 1')
    return 'done'


@outher_function
def some_function_2(param):
    print(f'some function 2')
    return 'done 2'


# other_fun = outher_function(some_function_2)
# other_fun()
print(some_function_1.__doc__)


def add(*args, **kwargs):
    print(kwargs)
    if 'testing_on' in kwargs:
        print('num6 has')
    print(args)


# add(1, 2, 3, 4, 5, testing_on=True, num=7)

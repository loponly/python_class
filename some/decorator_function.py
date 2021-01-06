

def outher_function(func):
    print(f'inner function {func}')

    def wrapper(param):
        print('other some things done 1')
        func(param)
        print('other some things done 2')

    return wrapper


@outher_function
def some_function_1(param):
    # print(param+1)
    print(f'some function 1')
    return 'done'


@outher_function
def some_function_2(param):
    print(f'some function 2')
    return 'done 2'


# other_fun = outher_function(some_function_2)
# other_fun()

some_function_2('2')

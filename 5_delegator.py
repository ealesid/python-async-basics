from inspect import getgeneratorstate


class MyException(Exception):
    pass


def coroutine(func):

    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except MyException:
            print('myexception:')
        except StopIteration:
            break
        else:
            print('.'*10, message)
    
    return 'returned from subgen()'


@coroutine
def delegator(g):

    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except MyException as e:
    #         g.throw(e)

    result = yield from g    # одной строкой заменили всю конструкцию выше
    print(result)

sg = subgen()
g = delegator(sg)

print(g.send('OK'))
g.throw(MyException)
g.throw(StopIteration)

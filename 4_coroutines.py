from inspect import getgeneratorstate


def coroutine(func):

    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('subgen received:', message)


class MyException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done!')
            break
        except MyException:
            print('.'*10)
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    
    return average


g = subgen()
print(getgeneratorstate(g))
g.send(None)
print(getgeneratorstate(g))
# g.send('OK')

a = average()
print(getgeneratorstate(a))
a.send(5)
a.send(3)
# a.throw(StopIteration)
# a.throw(MyException)

try:
    a.throw(StopIteration)
except StopIteration as e:
    print('Avereage', e.value)

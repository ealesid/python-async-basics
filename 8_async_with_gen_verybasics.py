from time import sleep


queue = []


def counter():
    counter = 0
    while True:
        print('counter >\t', counter)
        counter += 1
        yield


def printer():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('printer >\tprinting...')
        counter += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ == "__main__":

    queue.append(counter())
    queue.append(printer())

    main()

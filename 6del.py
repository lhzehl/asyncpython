def coroutines(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

    
class CustomException(Exception):
    pass



def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('XXxXxxxxxXX')
            break
        else:
            print('....', message)

    return 'string'


@coroutines
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except CustomException as e:
    #         g.throw(e)
    result = yield from g
    print(result)

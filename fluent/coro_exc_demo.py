"""
стр. 504
"""
class DemoException(Exception):
    """ Исключение для демонстрации """


def demo_exc_handling():
    print('-> сопрограмма стартовала')
    while True:
        try:
            x = yield
        except DemoException:  # Специальная обработка DemoException
            print('*** DemoException обработано. Продолжаем...')
        else:  # Если исключения не было, вывести полученное значение
            print('-> сопрограмма получила: {!r}'.format(x))
    raise RuntimeError('This line should never run.')

exc_coro = demo_exc_handling()
next(exc_coro)
# -> сопрограмма стартовала
exc_coro.send(11)
# -> сопрограмма получила: 11
exc_coro.send(22)
#-> сопрограмма получила: 22
exc_coro.close()
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))
# GEN_CLOSED
# Если методом throw передано исключение DemoException, то оно обрабатывается, и сопрограмма продолжается:
exc_coro = demo_exc_handling()
next(exc_coro)
# -> сопрограмма стартовала
exc_coro.send(11)
# -> сопрограмма получила: 11
exc_coro.throw(DemoException)
# *** DemoException обработано. Продолжаем...
print(getgeneratorstate(exc_coro))
# GEN_SUSPENED

# ЕСЛИ возбужденное в сопрограмме исключение не обработано, то она останавливается и переходит в состояние GEN_CLOSED
exc_coro = demo_exc_handling()
next(exc_coro)
# -> сопрограмма стартовала
exc_coro.send(11)
# -> сопрограмма получила: 11
exc_coro.throw(ZeroDivisionError)
# Traceback ...
print(getgeneratorstate(exc_coro))
# GEN_CLOSED

# Если необходимо, чтобы вне зависимости от способа завершения сопрограммы был выполнен какой-то код, 
# то соответствующую часть тела сопрограммы нужно обернуть блоком try/finally
def demo_exc_finally():
    print('-> сопрограмма стартовала')
    try:
        while True:
            try:
                x = yield
            except DemoException:  # Специальная обработка DemoException
                print('*** DemoException обработано. Продолжаем...')
            else:  # Если исключения не было, вывести полученное значение
                print('-> сопрограмма получила: {!r}'.format(x))
    finally:
        print('-> сопрограмма завершена')

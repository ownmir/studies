"""
A coroutine to compute a running average
Сопрограмма для вычисления скользящего среднего
coro_avg = averager()  # Вызываем averager(), она создает объект-генератор, который инициализируется в функции primer декоратора coroutine
from inspect import getgeneratorstate
getgeneratorstate(coro_avg)  # getgeneratorstate возвращает GEN_SUSPENDED, т.е. сопрограмма готова к приему значения.
# 'GEN_SUSPENDED'
coro_avg.send(10)  # Мы можем сразу же начать отправку значений coro_avg, в этом и состоял смысл декоратора
# 10.0
coro_avg.send(30)
20.0
coro_avg.send(5)
15.0
"""

from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    print('averager average', average, 'type',type(average))
    while True:
        print('averager in loop 8 average', average, 'type',type(average))
        term = yield average
        print('averager in loop 8 after yield average', average, 'type',type(average))
        total += term
        count += 1
        average = total/count

coro_avg = averager()  # Вызываем averager(), она создает объект-генератор, который инициализируется в функции primer декоратора coroutine
from inspect import getgeneratorstate
getgeneratorstate(coro_avg)  # getgeneratorstate возвращает GEN_SUSPENDED, т.е. сопрограмма готова к приему значения.
# 'GEN_SUSPENDED'
coro_avg.send(10)  # Мы можем сразу же начать отправку значений coro_avg, в этом и состоял смысл декоратора
# 10.0
coro_avg.send(30)
# 20.0
coro_avg.send(5)
# 15.0

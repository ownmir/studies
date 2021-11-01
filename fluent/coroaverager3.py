"""
стр 511
"""
from collections import namedtuple

Result = namedtuple('Result', 'count average')

# субгенератор
def averager():  # Та же сопрограмма, что в примере coroaverager2.py. Здесь это субгенератор
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # Каждое значение, отправленное клиентским кодом в main, здесь связывается с переменнной term.
        if term is None:  # Условие окончания. Без него выражение yield from, вызвавшее эту сопрограмму, оказалось бы навечно блокированным.
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # Возвращенное значение Result является значением выражения yield from в grouper.
 
# делегирующий генератор
def grouper(results, key):
   while True:  # На каждой итерации этого цикла создается новый экземпляр averager;
       # каждый из них является объектом-генератором, работающим как сопрограмма.
       results[key] = yield from averager()  # Значение, отправляемое генератору grouper, помещается выражением
       # yield from в канал, открытый с объектом averager.  
       # grouper остается приостановленным, пока averager потребляет значения, отправляемые клиентом.
       # Когда выполнение averager завершится, возвращенное им значение будет связано с results[key].
       # После этого в цикле while создается очередной экземпляр averager для потребления последующих значений.

# клиентский код или вызывающая сторона
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # объект-генератор. results - словарь, в котором будут собираться результаты. key - конкретный ключ этого словаря
        # Этот объект будет работать как сопрограмма.
        next(group)  # Инициализируем сопрограмму
        for value in values:
            group.send(value)  # Отправляем каждое значение value объекту grouper. Оно будет получено
            # в строке term = yield кода averager; grouper его никогда не увидит.
        group.send(None)  # важно! ! Отправка значения None объекту grouper приводит к завершению текущего
        # экземпляра averager и дает возможность grouper возобновить выполнение и создать очередной объект
        # averager для обработки следующей группы значений.
    # print(results)  # для отладки

# Вывод отчета
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))

data = {
    'girls;kg': [40.0, 50.0],
    'girls;m': [1.5, 1.6, 1.7],
    'boys;kg': [39.0, 40.0, 41.0],
    'boys;m': [1.3, 1.5]
}

if __name__ == '__main__':
    main(data)

import time
import functools

def clock1(func):
	"""Замыкание - это функция, которая запоминает привязки свободных переменных,
	существовавших на момент определения функции, так что их можно использовать впоследствии
	при вызове функции, когда область видимости, в которой она была определена, уже не существует
    
    время работы функции
	"""
	def clocked(*args):  # внутренняя функция (замыкание), принимающая произвольное число позиционных аргументов
		t0 = time.perf_counter()
		# эта функция работает только потому, что замыкание clocked
		result = func(*args)  # включает свободную переменную func
		elapsed = time.perf_counter() - t0  # пройденное время
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked  # возвращаем внутреннюю функцию взамен декорироемой

def clock(func):
    @functools.wraps(func) # wraps - обертывания
    def clocked(*args, **kwargs):
        # внутренняя функция (замыкание), принимающая произвольное число позиционных и именованых аргументов
        t0 = time.time()
        # эта функция работает только потому, что замыкание clocked
        result = func(*args, **kwargs)  # включает свободную переменную func
        elapsed = time.time() - t0  # пройденное время
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked  # возвращаем внутреннюю функцию взамен декорироемой

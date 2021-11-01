from functools import wraps

def coroutine(func):
    """Декоратор для инициализации сопрограмм"""
    @wraps(func)
    def primer(*args, **kwargs):  # Декораторированная генераторная функция подменяется этой функцией primer, которая при вызове возвращает инициализированный генератор
        print(func.__name__)
        gen = func(*args, **kwargs)  # Вызываем декорированную функцию, чтобы получить инициализированный генератор
        next(gen)  # Инициализируем генератор
        return gen  # Возвращаем его
    return primer
    
import time
from clock_decorator import clock1, clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
    print('*' * 35, 'Вызывается snooze(.123)')
    snooze(.123)
    print('*' * 35, 'Вызывается factorial(6)')
    print('6! =', factorial(6))

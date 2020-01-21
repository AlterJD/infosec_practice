from random import randrange, uniform

def miller_rabin(n, k):
    if n == 2:
        return True
    if not n and 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

n = 4

while not miller_rabin(n, 10):
    n = randrange(2 ** 49, 2 ** 50 - 1)
    
print('Найдено простое число: ', n, '\nДлина числа:', len(str(bin(n))) - 2)
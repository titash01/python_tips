# generate fibonacci

def fib(n:int) -> int:
    f0, f1 = 1,1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1
        print('swap')

fibs = list(fib(5))

print(fibs)
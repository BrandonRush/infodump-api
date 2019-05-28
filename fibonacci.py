# x = 0
# y = 1
# z = 0
# while x < 10000:
# 	print(x)
# 	z = x
# 	x += y
# 	y = z


# a,b=1,1
# while(True):
#   print(str(a) + "\n")
#   a,b=b,a+b       # Could also use b=a+b;a=b-a


# x_n = x_n-1 + x_n-2 for all n < 1

# history = {0: 0, 1: 1}
# def fib(x):
#     if x in history:
#         return history[x]
#     else:
#         history[x] = fib(x - 1) + fib(x - 2)
#     return history[x]
# def main():
#     for x in range(6, 10000):
#         print(fib(x))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    f = fib()
    for x in range(0, 100):
        print(next(f))


if __name__ == '__main__':
    main()

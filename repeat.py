def fib(n):
    f1, f2 = 1, 1
    result = [f1, f2]
    for i in range(n - 2):
        f = f1 + f2
        f1, f2 = f2, f
        result.append(f)
    return result


assert fib(1) == [1]
def fibo(n):
    if n < 0:
        raise ValueError
    elif n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    print(fibo(4))
    print("it work!")
    

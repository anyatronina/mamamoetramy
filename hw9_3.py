def printReversed(n):
    if n not in range(10):
        print(n % 10)
        printReversed(n // 10)
    else:
        print(n)

printReversed(123456789)
def digital_root(n):
    if n > 9:
        s = 0
        while n not in range(10):
            s += n % 10
            n = n // 10
        s += n  # суммируем последний элемент
        digit = digital_root(s)
    else:
        return n
    return digit

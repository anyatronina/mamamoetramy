def binaryDigit(n, b=[]):
    if n != 0 and n != 1:
        b.append(str(n % 2))
        return binaryDigit(n // 2, b)
    else:
        b.append(str(n))
        b.reverse()
        b_number = ''.join(b)
        return b_number


print(binaryDigit(13))
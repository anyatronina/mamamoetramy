def A(m, n):
    if m > 0:
        if n > 0:
            return A(m-1, A(m, n-1))
        else:
            return A(m-1, 1)
    else:
        return n + 1


print(A(1, 3))
print(A(4, 2))

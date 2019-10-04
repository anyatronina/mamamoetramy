a = int(input())
b = int(input())

alist = []
blist = []
while a != 0:
    alist.append(a % 10)
    a = a // 10
while b != 0:
    blist.append(b % 10)
    b = b // 10

if len(alist) > len(blist):
    for i in range(len(alist)-len(blist)):
        blist.append(0)
elif len(alist) < len(blist):
    for i in range(len(blist) - len(alist)):
        alist.append(0)


def summirovanie(p, q):
    clist = []
    k = 0
    for i in range(len(p)):
        clist.append(p[i] + q[i] + k)
        k = 0
        if clist[i] > 9:
            last = clist[i] // 10  # переменная для нового десятка в последнем действии
            clist[i] = clist[i] % 10
            k = 1
        else:
            last = 0
    if last != 0:
        clist.append(last)
    clist.reverse()
    return clist


def vichetanie(p, q):
    dlist = []
    k = 0
    if p[len(p)-1] == 0:
        m = p
        p = q
        q = m
        change = True
    else:
        change = False
    for i in range(len(p)):
        dlist.append(p[i] - q[i] - k)
        k = 0
        if dlist[i] < 0:
            dlist[i] = dlist[i] + 10
            k = 1
    dlist.reverse()
    if change:
        dlist[0] = - dlist[0]
    return dlist

print(vichetanie(alist,blist))
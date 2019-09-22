def palindrom(n):
    k=0 #количество цифр в числе
    m=n
    while m>0: #подсчет цифр
        k+=1
        m=m//10
    if k == 3:
        if n%10 == 0 and n//10%10 == n//100%10:
            return 'palindrom'
        else: 'ne palindrom'
    elif k == 4 and n//10%10 == n//100%10 and n%10 == n//1000:
        return 'palindrom'
    else:
        return 'ne palindrom'
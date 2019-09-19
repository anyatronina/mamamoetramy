def parking(day, hour):
    a = hour*100
    b = day % 2
    if 1900 <= a <= 2059:
        return 'both'
    elif (b == 0 and 2100 <= a <= 2359) or (b == 1 and 1859 >= a):
        return 'left'
    elif (b == 0 and 1859 >= a) or (b == 1 and 2100 <= a <= 2359):
        return 'right'

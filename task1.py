def parking(day, hour):
    b = day % 2
    if 19 <= a <= 20:
        return 'both'
    elif (b == 0 and 21 <= a <= 23) or (b == 1 and 18 >= a):
        return 'left'
    elif (b == 0 and 18 >= a) or (b == 1 and 21 <= a <= 23):
        return 'right'

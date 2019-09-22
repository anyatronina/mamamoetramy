def parking(day, hour):
    b = day % 2
    if 19 <= hour <= 20:
        return 'both'
    elif (b == 0 and 21 <= hour <= 23) or (b == 1 and 18 >= hour):
        return 'left'
    elif (b == 0 and 18 >= hour) or (b == 1 and 21 <= hour <= 23):
        return 'right'

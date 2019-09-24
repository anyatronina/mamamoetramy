# dist - расстояние от дома
# way - весь пройденный путь

n = 20


def working(m):
    dist = way = 0
    i = 1
    while i <= m:
        way += 1 / i
        if i % 2 == 1:
            dist += 1 / i
        else:
            dist -= 1 / i
        i += 1
    dist = int(dist * 100000) / 100000
    way = int(way * 100000) / 100000
    return dist, way


print(working(n))

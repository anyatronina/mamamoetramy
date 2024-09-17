class Room():
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.doors = []
        self.windows = []

    def add_window(self, window):
        self.windows.append(window)

    def add_door(self, door):
        self.doors.append(door)

    def wallpaper(self):
        s = 2*self.height*(self.length + self.width)
        for door in self.doors:
            s -= door.square()
        for window in self.windows:
            s -= window.square()
        return s

    def checkRoom(self):
        k = 0
        for window in self.windows:
            if window.height > self.height:
                k += 1
            else:
                if window.width > self.length and window.width > self.width:
                    k += 1
        for door in self.doors:
            if door.height > self.height:
                k += 1
            else:
                if door.width > self.length and door.width > self.width:
                    k += 1
        if k > 0:
            print('Комната не существует.')
        else:
            print('Комната существует.')


class Aperture():  # проём
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def square(self):
        return self.width*self.height


class Door(Aperture):
    def __init__(self, w, h):
        Aperture.__init__(self, w, h)


class Window(Aperture):
    def __init__(self, w, h, delta):
        Aperture.__init__(self, w, h)
        self.delta = delta


print('Введите длину*ширину*высоту комнаты:')
a = int(input())
b = int(input())
c = int(input())
room1 = Room(a, b, c)
print('Введите кол-во дверей:')
i = int(input())
if i != 0:
    for j in range(i):
        print('Введите высоту*ширину', j+1, '-й двери:')
        a = int(input())
        b = int(input())
        room1.add_door(Door(a, b))
print('Введите кол-во окон:')
i = int(input())
if i != 0:
    for j in range(i):
        print('Введите высоту*ширину', j+1, '-го окна:')
        a = int(input())
        b = int(input())
        print('Введите высоту от пола:')
        с = int(input())
        room1.add_window(Window(a, b, c))
room1.checkRoom()
print('Обоев нужно:', room1.wallpaper())
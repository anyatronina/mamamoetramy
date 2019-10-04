l = [2, 'cat', 7, 2, 9, 'cat', 7, 42]
new_l = []
for i in range(len(l)):
    if l[i] not in new_l:
        new_l.append(l[i])
l = new_l
print(l)
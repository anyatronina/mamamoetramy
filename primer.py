r = [{'1': 'a'}, {'2': 'b'}, {'3': 'c'}]
print(r[1].values())

for a in r:
    for key, val in a.items():
        print('{} #{}\n'.format(key, val))


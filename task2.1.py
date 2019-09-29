s = 'щядящий режим'
for i in range(len(s)):
    if s[i] == 'ж' or s[i] == 'ш' or s[i] == 'ч' or s[i] == 'щ' and s[i+1] != '':
        if s[i:i+2] == 'жи' or s[i:i+2] == 'ши':
            print(s[:i]+s[i:i+2].upper()+s[i+2:], '- верно')
        elif s[i:i+2] == 'ча' or s[i:i+2] == 'ща':
            print(s[:i]+s[i:i+2].upper()+s[i+2:], '- верно')
        elif s[i:i+2] == 'жы' or s[i:i+2] == 'шы':
            print('ошибка! пишется жи/ши:', s[:i]+s[i:i+2].upper()+s[i+2:])
        elif s[i:i+2] == 'чя' or s[i:i+2] == 'щя':
            print('ошибка! пишется ча/ща:', s[:i]+s[i:i+2].upper()+s[i+2:])
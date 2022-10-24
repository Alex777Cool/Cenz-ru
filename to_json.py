from json import dump

ar = []

with open('cenz-ru.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n !='':
            ar.append(n)

with open('cenz-ru.json', 'w', encoding='utf-8') as e:
    dump(ar, e)
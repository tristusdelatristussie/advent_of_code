day 1 

import numpy as np

text = """oneightwo4
oneeighthreeight
5oneeighthreeightonett
eezez5ezre
5zerere5trt57
1eightwo"""

number_mapping = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10'
}

first_num = []
last_num = []
tab = text.splitlines()

for line in tab:
    c=len(line)
    d=0
    for key, value in number_mapping.items():
        if line.find(value) > -1:
            if line.find(value) <=c:
                c = line.find(value)
                res = (c,int(value))
        elif line.find(key)> -1:
            if line.find(key) <=c:
                c = line.find(key)
                res = (c,int(value))
    first_num.append(res)
    
for line in tab:
    c=0
    for key, value in number_mapping.items():
        if line.rfind(value) > -1:
            if line.rfind(value) >=c:
                c = line.rfind(value)
                res = (c,int(value))
        elif line.rfind(key)> -1:
            if line.rfind(key) >=c:
                c = line.rfind(key)
                res = (c,int(value))
    last_num.append(res)
    
print(first_num)
print(last_num)


result = []

for t1, t2 in zip(first_num, last_num):
    elt_concat = str(t1[1]) + str(t2[1])
    result.append(int(elt_concat))

print(result)
print(np.sum(result))











day 2 part 1 et 2

p1 = 0
p2 = 0

for line in text.splitlines():
    games = line.split(':')[1]
    id_ = line.split(':')[0].split(' ')[1]
    ok = True
    cmax = {'red': 0, 'green': 0, 'blue': 0}
    for game in games.split(';'):
        for balls in game.split(','):
            b, c = balls.split()
            cmax[c] = max(cmax[c],int(b))
            if ok== True and int(b) > {'red': 12, 'green': 13, 'blue': 14}.get(c):
                ok = False
                print('jeux pas possibles :' , id_, game)
                p1 = p1 + int(id_)
    score = 1
    print(id_, cmax)
    for v in cmax.values():
        score = v * score
    p2 += score

print(p2)
print(p1)
            
            
day 3 part 1

tabs = []
tabsi = []
tabd = []
tabdi = []
tabtmp = []
tabtmpi = []
#offsets = [12, 11, 10, -10, -11, -12, +1, -1]
offsets = [142, 141, 140, -140, -141, -142, +1, -1]

gearsnum = []
f = False
for i , c in enumerate(text):
    if c!='.' and c!='\n' and not c.isdigit():
        tabs.append([i,c])
        tabsi.append(i)
for i , c in enumerate(text):
    if c.isdigit():
        tabtmp.append([i, c])
        tabtmpi.append(i)
        if any(i + offset in tabsi for offset in offsets):
            f = True
    elif f==True:
        tabd.append(tabtmp)
        tabdi.append(tabtmpi)
        tabtmp = []
        tabtmpi= []
        f= False
    else:
        tabtmp = []
        tabtmpi = []
        

        
tmp = [[t[1] for t in t] for t in tabd]
res = []
for r in tmp:
    res.append((int(''.join(r))))
sum(res)
    
#print([[t[1] for t in t] for t in tabd])
#print([[t[0] for t in t] for t in tabd])




            


day 3 part 2
gearsnumtmp = []
gearsnum = []
tabsi= []
#offsets = [12, 11, 10, -10, -11, -12, +1, -1]
offsets = [142, 141, 140, -140, -141, -142, +1, -1]

for i , c in enumerate(text):
    if c =='*':
        tabsi.append(i)
        
tmp = [[t[1] for t in t] for t in tabd]
res = []
for r in tmp:
    res.append((int(''.join(r))))

nbtmp = None
for s in tabsi:
    cpt = 0
    for nb , n in zip(res,tabdi):
        for i in n:
            if any(s  + offset == i for offset in offsets):
                cpt += 1
                nbtmp=nb
                gearsnumtmp.append(nbtmp)
                break
        if cpt==2 and nbtmp !=None:
            gearsnum.append(gearsnumtmp)
        nbtmp=None
    cpt=0
    gearsnumtmp = []
        
res = []
for l in gearsnum:
    res.append(sum(l))
    sum_result = sum(res)
    
res = []
for l in gearsnum:
    res.append(l[0]*l[1])
    prod_result = sum(res)

print('sum result =' , result)
print('prod result =' , prod_result)


day 4 part 1 

scores = 0
for lines in text.splitlines():
    id_, line = lines.split(':')
    cards, draws = line.split('|')
    cards = cards.split()
    draws = draws.split()
    cpt = 0
    v = 0
    score = 0
    last = 0
    for card in cards:
        if card in(draws):
            cpt += 1
            if cpt==1:
                v = 1
            else:
                v = v * 2
        score = v
    scores += score      
print('score total', scores)


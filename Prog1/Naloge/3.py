import math
'''Zapiši tri števila a b in c.'''
tester = False
while tester == False:
    try:
        a = float(input("a: "))
        if a != 0:
            tester = True
        else:
            print('a ne sme biti 0!')
    except:
        print("Ni realno število!")
tester = False
while tester == False:
    try:
        b = float(input("b: "))
        tester = True
    except:
        print("Ni realno število!")
tester = False
while tester == False:
    try:
        c = float(input("c: "))
        tester = True
    except:
        print("Ni  realno število!")
b = b / abs(a)
c = c / abs(a)
a = a / abs(a)
res1, res2 = 0, 0
diskriminanta = b**2 - 4*a*c
if diskriminanta < 0:
    print('Enačba nima realnih rešitev!')
else:
    res1 = (-b + math.sqrt(diskriminanta)) / 2*a
    res2 = (-b - math.sqrt(diskriminanta)) / 2*a
    print("Rešitvi: x1 = "+str(res1)+ " x2 = "+str(res2))

'''--------------------------------------------------------'''
niz = input("Vnesi poljuben niz: ")
tester = False
while tester == False:
    try:
        n = int(input("Vnesi število ponovitev (celo število): "))
        if n < 0:
            print("Ponovi! Število je manjše od 0.")
        else:
            tester = True
    except:
        print("Število ponovitev ni celo število!")
novi_niz = ""
for i in range(n):
    novi_niz += niz + ' '
novi_niz = novi_niz[:-1]
print(novi_niz)
    


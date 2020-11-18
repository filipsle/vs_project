from math import sqrt
"""
Projekt AK1VS - Trojúhelník
"""
"""
Fuknce pro výpočet délky stran.
Délka je počítána přesně, nicméně se v programu zobrazují pouze dvě desetinná místa.
a1, a2 jsou souřadnice bodu A; b1, b2 souřadnice bodu B
"""


def delka_strany(a1, a2, b1, b2):
    return sqrt(((b1-a1)**2)+((b2-a2)**2))


"""
Funkce určuje, jestli lze daný trojúhelník sestrojit.
Pokud ano, vrací 1, jinak 0. 
"""


def setrojitelnost(a1, b1, c1):
    if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
        return 1
    else:
        return 0


"""
Funkce počítá obvod trojúhelníku.
Počítá přesně, zobrazeny budou ale jen dvě desetinná čísla
"""


def obvod(a1, b1, c1):
    return a1+b1+c1


"""
Funkce počítá obsah pomocí Heronova vzorce, tudíž není potřeba znát výšku v trojúhelníku.
"""


def obsah(a1, b1, c1):
    s = (a1+b1+c1)/2
    return sqrt(s*(s-a1)*(s-b1)*(s-c1))


"""
Funkce pomocí Pythagorovy věty zjistí pravoúhlost trojúhelníku.
"""


def pravouhlost(a1, b1, c1):
    if c1**2 == (a1**2 + b1**2):
        return 1
    else:
        return 0


"""
Program začíná v tomto místě.
Uživatel je vyzván, aby zadal souřadnice bodů.
"""
ax = int(input("Zadej souřadnici x bodu A: "))
ay = int(input("Zadej souřadnici y bodu A: "))
bx = int(input("Zadej souřadnici x bodu B: "))
by = int(input("Zadej souřadnici y bodu B: "))
cx = int(input("Zadej souřadnici x bodu C: "))
cy = int(input("Zadej souřadnici y bodu C: "))

""""
Výpočet délek stran
"""
a = delka_strany(bx, by, cx, cy)
b = delka_strany(ax, ay, cx, cy)
c = delka_strany(ax, ay, bx, by)
print()
print("Délky stran:")
print("Délka strany a je ", "{:.2f}".format(a))
print("Délka strany b je ", "{:.2f}".format(b))
print("Délka strany c je ", "{:.2f}".format(c))
print()
if setrojitelnost(a, b, c):
    print("Zadaný trojúhelník lze setrojit.")
    print("Obvod trojúhelníku je ", "{:.2f}".format(obvod(a, b, c)))
    print("Obsah trojúhelníku je ", "{:.2f}".format(obsah(a, b, c)))
    if pravouhlost(a, b, c):
        print("Trojúhelník je pravoúhlý.")
    else:
        print("Trojúhelník není pravoúhlý.")
else:
    print("Zadaný trojúhelník neexistuje - nelze spočítat obvod a obsah ani určit pravoúhlost.")

"""
Note : 
- Char max ; 29
"""

import math

def main():
    while True:
        print("\nMode select\n===========\n1. Rad to Deg\n2. Deg to Rad\n3. Quit")
        gg = input("Mode : ")
        if gg == "1":
            RtD()
        elif gg == "2":
            DtR()
        elif gg == "3":
            break
        else:
            print("Choix invalide.")

def RtD():
    print("\nConversion radians → degres")
    f = input("Facteur de π (numerateur) : ")
    d = input("Denominateur de π : ")

    try:
        f = int(f)
        d = int(d)
        r = (f * math.π / d) * (180 / math.π)
        print("\n===============\n{}π/{} radians = {} degres".format(f, d, r))
    except ValueError:
        print("Erreur : valeur non valide.")

def DtR():
    print("\nConversion degres → radians")
    d = input("Degres : ")

    try:
        d = int(d) 
        num = d
        den = 180

        g = pgcd(abs(num), den)
        num //= g
        den //= g

        if num < 0:
            s = "-"
            num = -num
        else:
            s = ""

        if den == 1:
            print("\n===============\n{}° = {}π radians".format(d, s + str(num)))
        else:
            print("\n===============\n{}° = {}{}/{}π radians".format(d, s, num, den))
    except ValueError:
        print("Erreur : valeur non valide.")

# from the Frac.py LIB ; 1.0 & 30.9.25
def pgcd(a, b):
    """PGCD binaire (algorithme de Stein)"""
    if a == 0: return b
    if b == 0: return a
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1; b >>= 1; shift += 1
    while (a & 1) == 0:
        a >>= 1
    while b:
        while (b & 1) == 0: b >>= 1
        if a > b: a, b = b, a
        b -= a
    return a << shift


print("Robert Henning\n 24.9.2025 - 30.9.2025\n MIT Licenses\n Numworks Enchatements")
main()

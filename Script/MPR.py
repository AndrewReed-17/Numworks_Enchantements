import math

def main():
    while True:
        print("\nMode select\n===========\n1. Finding Main Measure\n0. Quit")
        gg = input("Mode : ")
        if gg == "1":
            FPM()
        elif gg == "0":
            break
        else:
            print("Choix invalide.")
            input("...")

def FPM():
    print("\nRadians → Mesure principale")
    f = input("Facteur de π (numerateur) : ")
    d = input("Denominateur de π : ")

    try:
        f = int(f)
        d = int(d)
        if d == 0:
            print("Erreur : denominateur nul.")
            return

        g = pgcd(abs(f), abs(d))
        f //= g
        d //= g

        # Gestion du signe
        s = "-" if f < 0 else ""
        f = abs(f)

        if d == 1:
            expr = "{}{}π".format(s, f)
        else:
            expr = "{}{}/{}π".format(s, f, d)

        if len(expr) > 29:
            expr = expr[:29]

        print("\n===============\nMesure principale = {}".format(expr))
        input("...")

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


print("Robert Henning\n30.9.2025\nMIT Licenses\nNumworks Enchantements")
main()

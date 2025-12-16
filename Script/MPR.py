from math import *

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

        # Angle en radians (float)
        theta = (f / d) * math.pi

        # Réduction dans [-pi, pi]
        theta = (theta + math.pi) % (2 * math.pi) - math.pi

        # Reconstruire fraction sur π
        ratio = theta / math.pi
        # approx fraction, mais bornée (éviter dénominateurs géants)
        from fractions import Fraction
        frac = Fraction(ratio).limit_denominator(12)

        num, den = frac.numerator, frac.denominator

        # Construction de l’expression
        if den == 1:
            expr = "{}π".format(num)
        elif num == 0:
            expr = "0"
        else:
            expr = "{}/{}π".format(num, den)
        if len(expr) > 29:
            expr = expr[:29]

        print("\n===============\nMesure principale = {}".format(expr))
        input("...")

    except ValueError:
        print("Erreur : valeur non valide.")

print("Robert Henning\n 30.9.2025\n MIT Licenses\n Numworks Enchantements | Github")
main()

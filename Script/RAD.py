import math

pi = math.pi

def main():
    while True:
        print("\nMode select")
        print("===========")
        print("1. Rad → Deg")
        print("2. Deg → Rad")
        print("0. Quit")

        gg = input("Mode : ")

        if gg == "1":
            RtD()
        elif gg == "2":
            DtR()
        elif gg == "0":
            break
        else:
            print("Choix invalide.")
            input("...")


def RtD():
    print("\nConversion radians → degrés")

    try:
        f = int(input("Facteur de π (numérateur) : "))
        d = int(input("Dénominateur de π : "))

        if d == 0:
            print("Erreur : dénominateur nul.")
            input("...")
            return

        # Conversion exacte
        num = 180 * f
        den = d

        g = pgcd(abs(num), abs(den))
        num //= g
        den //= g

        if den == 1:
            r = str(num)
        else:
            r = str(num) + "/" + str(den)

        print("\n================")
        print(str(f) + "π/" + str(d) + " radians = " + r + " degrés")

    except:
        print("Erreur : valeur non valide.")

    input("...")


def DtR():
    print("\nConversion degrés → radians")

    try:
        d = int(input("Degrés : "))

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

        print("\n================")
        if den == 1:
            print(str(d) + "° = " + s + str(num) + "π radians")
        else:
            print(str(d) + "° = " + s + str(num) + "/" + str(den) + "π radians")

    except:
        print("Erreur : valeur non valide.")

    input("...")


# PGCD binaire (Stein)
def pgcd(a, b):
    if a == 0: return b
    if b == 0: return a

    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    while (a & 1) == 0:
        a >>= 1

    while b:
        while (b & 1) == 0:
            b >>= 1
        if a > b:
            a, b = b, a
        b -= a

    return a << shift


print("Robert Henning\n 24.9.2025 - 16.12.2025\n MIT Licenses\n Numworks Enchatements \n GitHub")
main()

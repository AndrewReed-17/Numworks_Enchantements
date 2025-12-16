import math

pi = math.pi

def approx_frac(x, max_den=12):
    best_num = 0
    best_den = 1
    best_err = abs(x)

    for den in range(1, max_den + 1):
        num = round(x * den)
        err = abs(x - num / den)
        if err < best_err:
            best_err = err
            best_num = num
            best_den = den

    return best_num, best_den


def FPM():
    print("\nRadians → Mesure principale")

    try:
        f = int(input("Facteur de π (numérateur) : "))
        d = int(input("Dénominateur de π : "))

        if d == 0:
            print("Erreur : dénominateur nul.")
            return

        theta = (f / d) * pi
        theta = (theta + pi) % (2 * pi) - pi

        ratio = theta / pi
        num, den = approx_frac(ratio, 12)

        if num == 0:
            expr = "0"
        elif den == 1:
            expr = str(num) + "π"
        else:
            expr = str(num) + "/" + str(den) + "π"

        print("\n====================")
        print("Mesure principale =", expr)

    except:
        print("Erreur : entrée invalide.")


def main():
    while True:
        print("\nSélection du mode")
        print("=================")
        print("1. Mesure principale")
        print("0. Quitter")

        c = input("Mode : ")

        if c == "1":
            FPM()
        elif c == "0":
            break
        else:
            print("Choix invalide.")


print("Robert Henning\n 30.9.2025 - 16.12.2025 \n MIT Licenses\n Numworks Enchantements \n Github")
main()

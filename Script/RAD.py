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
    f = input("Facteur de Pi (numerateur) : ")
    d = input("Denominateur de Pi : ")

    try:
        f = int(f)
        d = int(d)
        r = (f * math.pi / d) * (180 / math.pi)
        print("\n===============\n{}pi/{} radians = {} degres".format(f, d, r))
    except ValueError:
        print("Erreur : valeur non valide.")

def DtR():
    print("\nConversion degres → radians")
    d = input("Degres : ")

    try:
        d = float(d)
        r = d * (math.pi / 180)
        print("\n===============\n{} degres = {} radians".format(d, r))
    except ValueError:
        print("Erreur : valeur non valide.")


print("Robert Henning, 24.9.2025.\n under the MIT Licenses\n part of the Numworks Enchantements collections")
main()

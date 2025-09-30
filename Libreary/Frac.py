""" 
A internal Lib to use in Python script that need a Rationnal Intiger Writting
Version : 1.0
DATE : 30.9.25
"""


SHIFT = 32        # largeur réservée au dénominateur (ici 32 bits)
MASK  = (1 << SHIFT) - 1

def pack(num, den):
    """Encode (num, den) en un seul entier"""
    if den == 0:
        raise ZeroDivisionError("ERR : DEN. nul")
    return (num << SHIFT) | (den & MASK)

def unpack(packed):
    """Décode un entier en (num, den)"""
    num = packed >> SHIFT
    den = packed & MASK
    return num, den

def pgcd(a, b):
    """PGCD binaire (Stein)"""
    if a == 0: return b
    if b == 0: return a
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1; b >>= 1; shift += 1
    while (a & 1) == 0: a >>= 1
    while b:
        while (b & 1) == 0: b >>= 1
        if a > b: a, b = b, a
        b -= a
    return a << shift

def add(p1, p2):
    """Addition de deux fractions encodées"""
    n1, d1 = unpack(p1)
    n2, d2 = unpack(p2)
    num = n1 * d2 + n2 * d1
    den = d1 * d2
    g = pgcd(abs(num), den)
    return pack(num // g, den // g)

def mul(p1, p2):
    """Multiplication de deux fractions encodées"""
    n1, d1 = unpack(p1)
    n2, d2 = unpack(p2)
    num = n1 * n2
    den = d1 * d2
    g = pgcd(abs(num), den)
    return pack(num // g, den // g)

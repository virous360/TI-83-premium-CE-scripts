"""
Calcule de Forces
Author : T.D. + A.N.
Date : 27/10/2023
version : 1
"""

masse_A = float(eval(input("Masse A = ")))
if int(input("1.kg\n2.g\n:")) == 2:
    masse_A = masse_A/1000

masse_B = float(eval(input("Masse B = ")))
if input("1.kg\n2.g\n:") == "2":
    masse_B = masse_B/1000

distance = float(eval(input("Distance(A/B) = ")))
if input("1.km\n2.m\n:") == "1":
    distance = distance/1000

G = float(input("G (0 for default) : "))
if G == 0:
    G = 6.67e-11

print("Force =", (G*masse_A*masse_B/distance**2), "N")

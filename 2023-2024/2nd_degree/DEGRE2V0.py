"""
Script : equations du second degree
Auth : Ali N.
Date : 1/11/2023
Version : 0
Special Characterset : ¹²³Delta
"""
from math import gcd

# CATEGORIE : Calcules

## Racines (WARNING : assumes Delta>0)
def Racines(a,b,c):
    D = b**2 - 4*a*c
    racine_delta = float(D**0.5)
    if racine_delta.is_integer():
        x1 = float((-b-racine_delta)/(2*a))
        x2 = float((-b+racine_delta)/(2*a))
        if not x1.is_integer():
            pgcd = gcd((-b-racine_delta),(2*a))
            x1 = (int((-b-racine_delta)/pgcd),int((2*a)/pgcd))
            x1 = str(x1[0])+"/"+str(x1[1])
        if not x2.is_integer():
            pgcd = gcd((-b+racine_delta),(2*a))
            x2 = (int((-b+racine_delta)/pgcd),int((2*a)/pgcd))
            x2 = str(x2[0])+"/"+str(x2[1])
        return (str(x1),str(x2))
    else :
        return (str(-b)+"-racine("+str(D)+")/"+str(2*a),str(-b)+"+racine("+str(D)+")/"+str(2*a))

## Racine (WARNING : assumes Delta = 0 )
def Racine(a,b):
    R = float(-b/(2*a))
    if R.is_integer():
        return (int(R),1)
    else : 
        pgcd = gcd(-b,2*a)
        return (int(-b/pgcd),int(2*a/pgcd))

# CATEGORIE : Convertir

## Canonique -> Develope : a(x-Alpha)²+Beta -> ax² + bx + c {Alpha=-b/2a ; Beta=-Delta/4a}
def can_to_dev(a,Alpha,Beta):
    return (a,-2*a*Alpha,a*(Alpha**2)-Beta)

## Factorise -> Develope : a(x-x1)(x-x2) -> ax² + bx + c
def fac_to_dev(a,x1,x2):
    return (a,-a*(x2+x1),a*(x1*x2))

## Factorise -> Develope : a(x-x0)² -> ax² + bx + c
def fac_to_dev2(a,x0):
    return (a,-2*a*x0,a*(x0**2))

## Develope -> Canonique : ax² + bx + c -> a(x-Alpha)²-Beta {Alpha=-b/2a ; Beta=-Delta/4a}
def dev_to_can(a,b,c):
    v = float(-(b**2 - 4*a*c)/(4*a))
    if v.is_integer():
        return (a,Racine(a,b),int(v))
    else:
        pgcd = gcd(-(b**2 - 4*a*c),4*a)
        return (a,Racine(a,b),(int(-(b**2 - 4*a*c)/pgcd),int(4*a/pgcd)))

## Develope -> Factorise
def dev_to_fact(a,b,c):
    D = b**2 - 4*a*c
    if D > 0 : # 2 racines reels
        x1,x2 = Racines(a,b,c)
        return "f(x) = "+str(a)+"(x-["+x1+"])(x-["+x2+"])" 
    elif D < 0 : # pas de racines dans l'ensemble R
        return "Pas de forme factorisee (Delta="+str(D)+"<0)"
    else: # Delta = 0 ; on admet une racine double
        r=Racine(a,b)
        if r[1] == 1 :
            return "f(x) = "+str(a)+"(x-"+str(r[0])+")²" 
        return "f(x) = "+str(a)+"(x-"+str(r[0])+"/"+str(r[1])+")²" 
        


# CATEGORIE : Points -> f(x)=ax²+bx+c

## Sommet + 1 Point
def sommet_point(xs,ys,x1,y1): # Sommet(Xs,Ys); Point(X1,Y1)
    a = float((y1-ys)/((x1-xs)**2))
    if a.is_integer() :
        return can_to_dev(int(a),xs,ys)
    else : 
        pgcd = gcd(y1-ys,(x1-xs)**2)
        return can_to_dev((int(y1-ys/pgcd),int((x1-xs)**2/pgcd)),xs,ys)

# Racines + 1 point 
def racines_point(x1,x2,x3,y3): # Racine 1 (X1;0) ; Racine 2 (X2;0) ; Point (X3;Y3)
    a = float(y3/((x3-x1)*(x3-x2)))
    if a.is_integer():
        return fac_to_dev(int(a),x1,x2)
    else :
        pgcd = gcd(y3,(x3-x1)*(x3-x2))
        return fac_to_dev((int(y3/pgcd),int((x3-x1)*(x3-x2)/pgcd)),x1,x2)

# Racine + 1 point 
def racine_point(x0,x3,y3): # Racine double (X0;0) ; Point (X3;Y3)
    a = float(y3/((x3-x0)**2))
    if a.is_integer() : 
        return fac_to_dev2(a,x0)
    else :
        pgcd = gcd(y3,(x3-x0)**2)
        return fac_to_dev2((int(y3/pgcd),int((x3-x0)**2/pgcd)),x0)
    
# 3 points (ordonnees)
def trois_points(x1,y1,x2,y2,x3,y3):
    b1 = (y3-y1)*((x2**2)-(x1**2))-(y2-y1)*((x3**2)-(x1**2))
    b2 = (x3-x1)*((x2**2)-(x1**2))-(x2-x1)*((x3**2)-(x1**2))
    b = float(b1/b2)
    if b.is_integer():
        b = int(b)
    else:
        pgcd = gcd(b1,b2)
        b = (int(b1/pgcd),int(b2/pgcd))
    
    a1= (y2-y1-b*(x2-x1))
    a2= ((x2**2)-(x1**2))
    a = float(a1/a2)
    if a.is_integer():
        a = int(a)
    else:
        pgcd = gcd(a1,a2)
        a = (int(a1/pgcd),int(a2/pgcd))
    
    c = float(y1-(x1**2)*a-x1*b)
    return (a,b,c)

# CATEGORIE : equ. Bicaree / 2 points (S;P)

# equ. Bicaree : a x^4 + b x^2 + c = 0 
def Bicarre(a,b,c):
    D = b**2 - 4*a*c
    if D > 0 : # 2 racines reels
        x1,x2 = Racines(a,b,c)
        return ("racine["+x1+"]","-racine["+x1+"]","racine["+x2+"]","-racine["+x2+"]") 
    elif D < 0 : # pas de racines dans l'ensemble R
        return "Pas de racines (Delta="+str(D)+"<0)"
    else: # Delta = 0 ; on admet une racine double
        r = Racine(a,b)
        if r[1] == 1:
            r0 = float(r[0]**(0.5))
            if r0.is_integer():
                return (str(r0),str(-r0)) 
            else:
                return ("racine["+str(r[0])+"]","-racine["+str(r[0])+"]") 
        else :
            return ("racine["+str(r[0])+"/"+str(r[1])+"]","-racine["+str(r[0])+"/"+str(r[1])+"]")

def somme_produit(S,P):
    a,b,c = (1,-S,P)
    D = b**2 - 4*a*c
    if D > 0 : # 2 racines reels
        x1,x2 = Racines(a,b,c)
        return (x1,x2) 
    elif D < 0 : # pas de racines dans l'ensemble R
        return "Pas de nombres ayan S comme somme et P comme produit (Delta="+str(D)+"<0)"
    else: # Delta = 0 ; on admet une racine double
        return (Racine(a,b)) 

Catego = int(input("""1.Convertir (facto,dev,cano)
2.Calcule (Alpha,Beta,racines,Delta)
3.Trouver une fonction
4.Equation bicarre
5.2 Points avec S et P
:"""))
if (0 < Catego < 6):
    if Catego == 1: #1.Convertir (facto,dev,cano)
        Convertir = int(input("""=============input==============
1.Canonique
2.Factorise
3.Develope
:"""))
        if (0 < Convertir < 4):
            if Convertir == 1 : #1.Canonique
                a = float(eval(input("""===========Canonique============
f(x) = a(x-Alpha)²-Beta 
{Alpha=-b/2a ; Beta=-Delta/4a}
a=""")))
                alpha = float(eval(input("Alpha=")))
                beta = float(eval(input("Beta=")))
                print("="*32)
                dev = can_to_dev(a,alpha,beta)
                print("Develope: ")
                print("f(x) = "+str(dev[0])+"x² + "+str(dev[1])+"x + "+str(dev[2]))
                fact = dev_to_fact(dev[0],dev[1],dev[2])
                print("Factorise: ")
                print(fact)
                
                
                
                
print("==============fin===============")
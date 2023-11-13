from math import gcd
def Delta(a,b,c):
    return b**2 - 4*a*c
def Racines(a,b,c):
    RDelta = float(Delta(a,b,c)**0.5)
    if RDelta.is_integer():
        x1 = float((-b-RDelta)/(2*a))
        x2 = float((-b+RDelta)/(2*a))
        if not x1.is_integer():
            pgcd = gcd((-b-RDelta),(2*a))
            x1 = (int((-b-RDelta)/pgcd),int((2*a)/pgcd))
            x1 = str(x1[0])+"/"+str(x1[1])
        if not x2.is_integer():
            pgcd = gcd((-b+RDelta),(2*a))
            x2 = (int((-b+RDelta)/pgcd),int((2*a)/pgcd))
            x2 = str(x2[0])+"/"+str(x2[1])
        return (str(x1),str(x2))
    else :
        return (str(-b)+"-racine("+str(Delta(a,b,c))+")/"+str(2*a),str(-b)+"+racine("+str(Delta(a,b,c))+")/"+str(2*a))
def Racine(a,b):
    return (float(-b/(2*a)),1)
    # if Ra.is_integer():
    #     return (int(Ra),1)
    # else : 
    #     pgcd = gcd(-b,2*a)
    #     return (int(-b/pgcd),int(2*a/pgcd))
def fac_to_dev(a,x1,x2):
    return (a,-a*(x2+x1),a*(x1*x2))
def fac_to_dev2(a,x0):
    return (a,-2*a*x0,a*(x0**2))
def dev_to_can(a,b,c):
    v = float(-Delta(a,b,c)/(4*a))
    if v.is_integer():
        return (a,Racine(a,b),int(v))
    else:
        pgcd = gcd(-Delta(a,b,c),4*a)
        return (a,Racine(a,b),(int(-Delta(a,b,c)/pgcd),int(4*a/pgcd)))
def dev_to_fact(a,b,c):
    if Delta(a,b,c) > 0 : 
        x1,x2 = Racines(a,b,c)
        return "f(x) = "+str(a)+"(x-["+x1+"])(x-["+x2+"])" 
    elif Delta(a,b,c) < 0 : 
        return "Pas de forme factorisee (Delta="+str(Delta(a,b,c))+"<0)"
    else: 
        r=Racine(a,b)
        if r[1] == 1 :
            return "f(x) = "+str(a)+"(x-"+str(r[0])+")²" 
        return "f(x) = "+str(a)+"(x-"+str(r[0])+"/"+str(r[1])+")²" 
def sommet_point(xs,ys,x1,y1): 
    a = float((y1-ys)/((x1-xs)**2))
    if a.is_integer() :
        a=int(a)
        return (a,-2*a*xs,a*(xs**2)-ys)
    else : 
        pgcd = gcd(y1-ys,(x1-xs)**2)
        return ((int(y1-ys/pgcd),int((x1-xs)**2/pgcd)),-2*(int(y1-ys/pgcd),int((x1-xs)**2/pgcd))*xs,(int(y1-ys/pgcd),int((x1-xs)**2/pgcd))*(xs**2)-ys)
def racines_point(x1,x2,x3,y3): 
    a = float(y3/((x3-x1)*(x3-x2)))
    if a.is_integer():
        return fac_to_dev(int(a),x1,x2)
    else :
        pgcd = gcd(y3,(x3-x1)*(x3-x2))
        return fac_to_dev((int(y3/pgcd),int((x3-x1)*(x3-x2)/pgcd)),x1,x2)
def racine_point(x0,x3,y3): 
    a = float(y3/((x3-x0)**2))
    if a.is_integer() : 
        return fac_to_dev2(a,x0)
    else :
        pgcd = gcd(y3,(x3-x0)**2)
        return fac_to_dev2((int(y3/pgcd),int((x3-x0)**2/pgcd)),x0)
def trois_points(x1,y1,x2,y2,x3,y3):
    b = float(((y3-y1)*((x2**2)-(x1**2))-(y2-y1)*((x3**2)-(x1**2)))/((x3-x1)*((x2**2)-(x1**2))-(x2-x1)*((x3**2)-(x1**2))))
    if b.is_integer():
        b = int(b)
    else:
        pgcd = gcd(((y3-y1)*((x2**2)-(x1**2))-(y2-y1)*((x3**2)-(x1**2))),((x3-x1)*((x2**2)-(x1**2))-(x2-x1)*((x3**2)-(x1**2))))
        b = (int(((y3-y1)*((x2**2)-(x1**2))-(y2-y1)*((x3**2)-(x1**2)))/pgcd),int(((x3-x1)*((x2**2)-(x1**2))-(x2-x1)*((x3**2)-(x1**2)))/pgcd))
    a = float(((y2-y1-b*(x2-x1)))/(((x2**2)-(x1**2))))
    if a.is_integer():
        a = int(a)
    else:
        pgcd = gcd(((y2-y1-b*(x2-x1))),(((x2**2)-(x1**2))))
        a = (int(((y2-y1-b*(x2-x1)))/pgcd),int((((x2**2)-(x1**2)))/pgcd))
    c = float(y1-(x1**2)*a-x1*b)
    return (a,b,c)
def Bicarre(a,b,c):
    D = Delta(a,b,c)
    if D > 0 : 
        x1,x2 = Racines(a,b,c)
        return ("racine["+x1+"]","-racine["+x1+"]","racine["+x2+"]","-racine["+x2+"]") 
    elif D < 0 : 
        return "Pas de racines (Delta="+str(D)+"<0)"
    else: 
        r = Racine(a,b)
        # if r[1] == 1:
        r0 = float(r[0]**0.5)
        if r0.is_integer():
            return (str(r0),str(-r0)) 
        else:
            return ("racine["+str(r[0])+"]","-racine["+str(r[0])+"]") 
        # else :
        #     return ("racine["+str(r[0])+"/"+str(r[1])+"]","-racine["+str(r[0])+"/"+str(r[1])+"]")
def somme_produit(S,P):
    a,b,c = (1,-S,P)
    D = Delta(a,b,c)
    if D > 0 : 
        x1,x2 = Racines(a,b,c)
        return (x1,x2) 
    elif D < 0 : 
        return "Pas de nombres ayan S comme somme et P comme produit (Delta="+str(D)+"<0)"
    else: 
        return (Racine(a,b)) 
Catego = int(input("""1.Convertir (facto,dev,cano)
2.Calcule (Alpha,Beta,racines,Delta)
3.Trouver une fonction
4.Equation bicarre
5.2 Points avec S et P
:"""))
if (0 < Catego < 6):
    if Catego == 1: 
        Convertir = int(input("""=============input==============
1.Canonique
2.Factorise
3.Develope
:"""))
        if (0 < Convertir < 4):
            if Convertir == 1 : 
                a = float(eval(input("""===========Canonique============
f(x) = a(x-Alpha)²-Beta 
{Alpha=-b/2a ; Beta=-Delta/4a}
a=""")))
                alpha = float(eval(input("Alpha=")))
                beta = float(eval(input("Beta=")))
                print("="*32)
                dev = (a,-2*a*alpha,a*(alpha**2)-beta)
                print("Develope: ")
                print("f(x) = "+str(dev[0])+"x² + "+str(dev[1])+"x + "+str(dev[2]))
                fact = dev_to_fact(dev[0],dev[1],dev[2])
                print("Factorise: ")
                print(fact)
                
                
                
                
print("==============fin===============")
'''python3.9.13 ; absolute value ; version 2.0
Ali Naim ; 10/6/2022
'''
def abs_to_interval_ineq():
    print("format : |x-c| =/>/</<=/>= r ")
    c = int(input("c = "))
    opp = input("""1 : = 
2 : >
3 : < 
4 : <=
5 : >=
""")
    r = int(input("r = "))
    cmr = str(c - r)
    cpr = str(c + r)
    print("=====================")
    if opp == "2" and r<0:
        print("S = |R = ]-inf;+inf[")
    elif opp == "5" and r<0 :
        print("S = |R = ]-inf;+inf[")
    elif opp == "3" and r<0:
        print("S = phi = {}")
    elif opp == "4" and r == 0:
        print ("x = "+str(c))
    elif opp == "1":
        print ("x="+cmr+" or x="+cpr+" ; S={"+cmr+" ; "+cpr+"}")
    elif opp == "2":
        print("x ]"+cmr+";"+cpr+"[")
        print(cmr + " < x < " + cpr)
    elif opp == "3":
        print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[")
        print("x < " + cmr + " et x > " + cpr)
    elif opp == "4":
        print("x ["+cmr+';'+cpr+']')
        print(cmr + " <= x <= " + cpr)
    elif opp == "5":
        print("x ]-inf;"+cmr+"]U["+cpr+";+inf[")
        print("x <= " + cmr + " et x >= " + cpr)
def ineq_to_abs():
    opp = input("""
1. *1 < x < *2
2. *1 <= x <= *2
3. x < *1 et x > *2
4. x <= *1 et x >= *2
""")
    cmr = int(input("*1 = "))
    cpr = int(input("*2 = "))
    c = str(int((cpr + cmr)/2))
    r = str(int(cpr - int(c)))
    cmr = str(cmr)
    cpr = str(cpr)
    if opp == "1":
        print("x ]"+cmr+";"+cpr+"[")
        print("|x - "+ c + "| < " + r)
    elif opp == "2":
        print("x ["+cmr+';'+cpr+']')
        print("|x - "+ c + "| <= " + r)
    elif opp == "3":
        print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[")
        print("|x - "+ c + "| > " + r)
    elif opp == "4" : 
        print("x ]-inf;"+cmr+"]U["+cpr+";+inf[")
        print("|x - "+ c + "| >= " + r)
def interval_to_abs():
    opp = input("""
1. x ]*1;*2[
2. x [*1;*2]
3. x ]-inf;*1[U]*2;+inf[2

4. x ]-inf;*1]U[*2;+inf[
""")
    cmr = int(input("*1 = "))
    cpr = int(input("*2 = "))
    c = str(int((cpr + cmr)/2))
    r = str(int(cpr - int(c)))
    cmr = str(cmr)
    cpr = str(cpr)
    if opp == "1":
        print(cmr+" < x < "+cpr)
        print("|x - "+ c + "| < " + r)
    elif opp == "2":
        print(cmr+' <= x <= '+cpr)
        print("|x - "+ c + "| <= " + r)
    elif opp == "3":
        print("x < "+cmr+" et x > "+cpr)
        print("|x - "+ c + "| > " + r)
    elif opp == "4" : 
        print("x <= "+cmr+" et x >= "+cpr)
        print("|x - "+ c + "| >= " + r)
        
main1 = input("""
1. abs input
2. ineq input
3. interval input 
""")
if main1 == "1":
    abs_to_interval_ineq()
elif main1 == "2" :
    ineq_to_abs()
else :
    interval_to_abs()
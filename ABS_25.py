'''python3.9.13 ; absolute value ; version 2.5
Ali Naim ; 10/7/2022
'''

#input absolute value and output interval / inequation form
def abs_to_interval_ineq():
    #print the syntax of the absolute value 
    print("format : |x-c| =/>/</<=/>= r ")
    # c=center ; input center as int (to add: check for int no not have errors)
    c = int(input("c = "))
    # opp=opperator ; the input is an int to symplify usage on calculators (to add: check for int from 1 to 5  no not have errors)
    opp = input("""1 : = 
2 : >
3 : < 
4 : <=
5 : >=
""")
    # r=radius ; (to add: check for int no not have errors)
    r = int(input("r = "))
    cmr = str(c - r)
    cpr = str(c + r)
    #break print to separate input from answer 
    print("=====================")
    # exeptions
    if opp == "2" and r<0:
        print("S = |R = ]-inf;+inf[")
    elif opp == "5" and r<0 :
        print("S = |R = ]-inf;+inf[")
    elif opp == "3" and r<0:
        print("S = phi = {}")
    elif opp == "4" and r == 0:
        print ("x = "+str(c))
    # usual opperations 
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
# input inequation ; out abs and interval
def ineq_to_abs():
    #choose a syntax for the ineqation (int check + [1,4])
    opp = input("""
1. *1 < x < *2
2. *1 <= x <= *2
3. x < *1 et x > *2
4. x <= *1 et x >= *2
""")
    # *1 represents c - r and *2 represents c + r
    cmr = int(input("*1 = "))
    cpr = int(input("*2 = "))
    # if cmr > cpr than the inequation is wrong 
    if cmr > cpr:
        print("error")
        exit()
    # (c + r) + (c - r) = 2c ; Ans/2 = c ... r = c+r - c 
    c = str(int((cpr + cmr)/2))
    r = str(int(cpr - int(c)))
    # redifine cmr and cpr to be used as str after completing calculations 
    cmr = str(cmr)
    cpr = str(cpr)
    # exeptions 
    if opp == "1" and cmr==cpr:
        print("S = phi = {}")
    elif opp == "3" and cmr==cpr:
        print("S = phi = {}")
    elif opp == "2" and cmr==cpr :
        print("x = " + cmr)
    elif opp == "4" and cmr==cpr:
        print("x = " + cmr)
    # normal execution 
    elif opp == "1":
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
# input interval ; output abs and inequation
def interval_to_abs():
    # input opperator (syntax)
    opp = input("""
1. x ]*1;*2[
2. x [*1;*2]
3. x ]-inf;*1[U]*2;+inf[2

4. x ]-inf;*1]U[*2;+inf[
""")
    # input 
    cmr = int(input("*1 = "))
    cpr = int(input("*2 = "))
    #check for errors 
    if cmr > cpr:
        print("error")
        exit()
    #calculate c and r 
    c = str(int((cpr + cmr)/2))
    r = str(int(cpr - int(c)))
    #convert to str after calculations
    cmr = str(cmr)
    cpr = str(cpr)
    # ...
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
# main1 is the first menu that asks the user for the type of input 
main1 = input("""1. abs input
2. ineq input
3. interval input
:""")
if main1 == "1":
    abs_to_interval_ineq()
elif main1 == "2" :
    ineq_to_abs()
elif main1 == "3":
    interval_to_abs()
def f1():
 print("format : |x-c| =/>/</<=/>= r ")
 c=int(input("c = "))
 opp=input("""1 : = 
2 : >
3 : < 
4 : <=
5 : >=
""")
 opp=int(opp)
 r=int(input("r = "))
 cmr=str(c - r);cpr=str(c + r);print("=====================")
 if opp==2 and r<0:
  print("S = |R = ]-inf;+inf[")
 elif opp==5 and r<0:
  print("S = |R = ]-inf;+inf[")
 elif opp==3 and r<0:
  print("S = phi = {}")
 elif opp==4 and r==0:
  print ("x = "+str(c))
 elif opp==1:
  print ("x="+cmr+" or x="+cpr+" ; S={"+cmr+" ; "+cpr+"}")
 elif opp==3:
  print("x ]"+cmr+";"+cpr+"[");print(cmr + " < x < " + cpr)
 elif opp==2:
  print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[");print("x < " + cmr + " et x > " + cpr)
 elif opp==4:
  print("x ["+cmr+';'+cpr+']');print(cmr + " <= x <= " + cpr)
 elif opp==5:
  print("x ]-inf;"+cmr+"]U["+cpr+";+inf[");print("x <= " + cmr + " et x >= " + cpr)
def f2():
 opp=input("""
1. *1 < x < *2
2. *1 <= x <= *2
3. x < *1 et x > *2
4. x <= *1 et x >= *2
5. x > *1 |6. x < *1 
7. x >= *1 |8. x <= *1
""")
 opp=int(opp)
 cmr=int(input("*1 = "))
 cpr=int(input("*2="))
 c=str(int((cpr + cmr)/2));r=str(int(cpr - int(c)));cmr=str(cmr);cpr=str(cpr)
 if opp==1 and cmr==cpr:
  print("S = phi = {}")
 elif opp==3 and cmr==cpr:
  print("S = phi = {}")
 elif opp==2 and cmr==cpr:
  print("x = " + cmr)
 elif opp==4 and cmr==cpr:
  print("x = " + cmr)
 elif opp==1:
  print("x ]"+cmr+";"+cpr+"[");print("|x - "+ c + "| < " + r)
 elif opp==2:
  print("x ["+cmr+';'+cpr+']');print("|x - "+ c + "| <= " + r)
 elif opp==3:
  print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[");print("|x - "+ c + "| > " + r)
 elif opp==4: 
  print("x ]-inf;"+cmr+"]U["+cpr+";+inf[");print("|x - "+ c + "| >= " + r)
 elif opp==5:
  print("x ]" + cmr + ", +inf[")
 elif opp==6:
  print("x ]-inf," + cmr + "[")
 elif opp==7:
  print("x [" + cmr + ", +inf[")
 elif opp==8:
  print("x ]-inf," + cmr + "]")
def f3():
 opp=input("""
1. x ]*1;*2[
2. x [*1;*2]
3. x ]-inf;*1[U]*2;+inf[
4. x ]-inf;*1]U[*2;+inf[
5. x ]-inf,*1[ |6. x ]*1,+inf[
7. x ]-inf,*1] |8. x [*1,+inf[ 
""")
 opp=int(opp)
 cmr=int(input("*1 = "))
 cpr=int(input("*2 = "))
 c=str(int((cpr + cmr)/2));r=str(int(cpr - int(c)));cmr=str(cmr);cpr=str(cpr)
 if opp==1:
  print(cmr+" < x < "+cpr);print("|x - "+ c + "| < " + r)
 elif opp==2:
  print(cmr+' <= x <= '+cpr);print("|x - "+ c + "| <= " + r)
 elif opp==3:
  print("x < "+cmr+" et x > "+cpr);print("|x - "+ c + "| > " + r)
 elif opp==4: 
  print("x <= "+cmr+" et x >= "+cpr);print("|x - "+ c + "| >= " + r)
 elif opp==5:
  print("x < " + cmr )
 elif opp==6:
  print("x > " + cmr )
 elif opp==7:
  print("x <= " + cmr )
 elif opp==8:
  print("x >= " + cmr)
main1=input("""1. abs input
2. ineq input
3. interval input
:""")
main1=int(main1)
if main1==1:
  f1()
elif main1==2:
 f2()
elif main1==3:
 f3()
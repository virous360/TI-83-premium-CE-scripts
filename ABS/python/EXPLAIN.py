# fonction qui permet d'entrer une valeur absolue et avoir son equivalent sous forme d’inéquation et d'intervale
#définir (def) fonction 1 (abs_input) : 
def abs_input():
# l'espace est nécessaire pour marquer toutes les commandes appartenant a cette fonction
 # imprimer le format pour indiquer a l'utilisateur la forme de l'expression qui va être calculer 
 print("format : |x-c| =/>/</<=/>= r ")
 # le centre (c) est indiquer par l'utilisateur, il est ensuite convertie en float() pour être utilise en calcule. il est ensuite arrondie avec 1 nombre decimal apres la virgule (round(*,2))
 c=round(float(input("c = ")),2)
# on utilise opp comme menu qui permet de choisir un opérateur de calcule. convertie en int() pour simplifier la comparaison (NOTE: si ont ne convertie pas, quand on vas comparais on utilise str "1" au lieu de int "1"... )
 opp=int(input("""1 : = 
2 : >
3 : < 
4 : <=
5 : >=
"""))
# définir le rayon; le rayon et le centre peuvent être utiliser pour le calcule d’après c-r et c+r
 r=round(float(input("r = ")),2)
# définir c-r et arrondir puis c + r 
 cmr=str(round(c - r,2))
 cpr=str(round(c + r,2))
#imprimer un séparateur (non nécessaire)
 print("=====================")
#  exceptions :
 if opp==2 and r<0: # si > et r<0 (la valeur absolue est toujours > qu'un nombre negative donc la solution est R)
  print("S = |R = ]-inf;+inf[")
 elif opp==5 and r<0: # si >= et r<0 (la valeur absolue est toujours > qu'un nombre negative donc la solution est R)
  print("S = |R = ]-inf;+inf[")
 elif opp==3 and r<0: # si abs<0 (abs negative) or une valeur absolue n'est jamais negative 
  print("S = phi = {}")
 elif opp==4 and r==0: # <= 0 ; |x-c|<=0 ; c-r = c-0 = c ; et c+r = c+0 = c
  print ("x = "+str(c))
 elif opp==1: # =
  print ("x="+cmr+" or x="+cpr+" ; S={"+cmr+" ; "+cpr+"}")
 elif opp==3: # >
  print("x ]"+cmr+";"+cpr+"[")
  print(cmr + " < x < " + cpr)
 elif opp==2: # <
  print("x ]-inf;"+cmr+"[U]"+cpr+";+inf[");print("x < " + cmr + " et x > " + cpr)
 elif opp==4: # <=
  print("x ["+cmr+';'+cpr+']');print(cmr + " <= x <= " + cpr)
 elif opp==5: # >=
  print("x ]-inf;"+cmr+"]U["+cpr+";+inf[");print("x <= " + cmr + " et x >= " + cpr)
#définir (def) fonction 2 (inéquation_input) : 
def ineq_input():
 opp=input("""
1. *1 < x < *2
2. *1 <= x <= *2
3. x < *1 et x > *2
4. x <= *1 et x >= *2
5. x > *1 |6. x < *1 
7. x >= *1 |8. x <= *1
""")
 opp=int(opp)
 cmr=round(float(input("*1 = ")),2)
 cpr=round(float(input("*2 = ")),2)
 c=str(round(float((cpr + cmr)/2),2));r=str(round(float(cpr) - float(c),2));cmr=str(cmr);cpr=str(cpr)
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
 opp=round(float(opp),2)
 cmr=round(float(input("*1 = ")),2)
 cpr=round(float(input("*2 = ")),2)
 c=str(round((cpr + cmr)/2,2));r=str(round(cpr - float(c),2));cmr=str(cmr);cpr=str(cpr)
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
main1=round(float(main1),2)
if main1==1:
 abs_input()
elif main1==2:
 ineq_input()
elif main1==3:
 f3()
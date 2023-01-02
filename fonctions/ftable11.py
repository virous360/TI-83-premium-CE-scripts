#test remake 2
from math import *
print("-"*32)
fx = input("f(x) : ")
if fx.endswith(")"):
    fx += "=0"
fx = fx.split(")")
opp = fx.pop()[:-1]
fx = [x[1:] for x in fx]
list_inter = [] #proccess each input :
for index,opperation in enumerate(fx):
    p = False
    opperation = opperation.split("x") # [1]=c ; [0] = k 
    if opperation[0] == "":
        before_x = "1"
    elif opperation[0] == "-":
        before_x = "-1"
    elif opperation[0].endswith("^"):#used to indicate x^2
        if "S" in opperation[0]:
            opperation[0] = opperation[0].replace("S","sqrt(")[:-1] + ")^"
        before_x = eval(opperation[0][:-1])
        p = True
    else:
        if "S" in opperation[0]:
            opperation[0] = opperation[0].replace("S","sqrt(")+ ")"
        before_x = eval(opperation[0])
    if "S" in opperation[1]:
            opperation[1] = opperation[1].replace("S","sqrt(")+ ")"
    after_x = eval(opperation[1])
    if float(before_x) < 0 :
        if opp == ">": opp = "<"
        elif opp == "<": opp = ">"
        elif opp == ">=": opp = "<="
        elif opp == "<=": opp = ">="
    after_x = float(after_x)/float(before_x)
    if p:
        if after_x>0 :#ex : x^2 + 3 =0 ; x^2 = -3 ; x = sqrt(-3)
            print("math error:")
            exit()
        after_x = sqrt(abs(after_x))
    fx[index] = float(after_x)
    list_inter.append(float(after_x)*-1)
    if p:
        fx.append(float(after_x)*-1)
        list_inter.append(float(after_x))
print("-"*32)
list_inter.sort()
list_inter = [str(x)[:5] for x in list_inter]
table_head = "-inf | "+" | ".join(list_inter)+" | +inf"
if len(table_head) > 32:
    print("table is too big... can't print")
    print("inter:"+"|".join(list_inter))
else:
    print(table_head)
    print("-"*len(table_head))
dic_sign = {intersection: "-"*(index+1) + "+"*(len(list_inter)-index) for index,intersection in enumerate(list_inter)}
list_signs = [dic_sign[str(i)] for i in list_inter]
final = ""
for i in [[sign_array[i] for sign_array in list_signs] for i in range(len(list_signs[0]))]:
    temp = 1
    for x in i:
        if x == "-":
            temp *= -1
    if temp == -1:
        final += "-"
    else:
        final += "+"
for i in list_inter:
    if float(i) >=0 : 
        y = "+"+str(i)
    else:
        y = str(i)
    print("({:6}) : {}".format("x"+y,dic_sign[str(i)]))
print("Solution : "+final)## solve x
table_head_elements = list(list_inter)
table_head_elements.insert(0,"-inf")
table_head_elements.append("+inf")
if opp == "=":
    print(list_inter)
    exit()
intervals = [[],[]] #with [0] for - and [1] for + 
for index,sign in enumerate(final):
    if sign == "+inf":
        pass
    if sign == "-":
        intervals[0].append([table_head_elements[index],table_head_elements[index+1]])
    else:
        intervals[1].append([table_head_elements[index],table_head_elements[index+1]])
for i in range(2):
    for index,array in enumerate(intervals[i]):#list[str,str]
        if array[0] == "-inf":
            intervals[i][index] = "]"+",".join(array)
            if "=" in opp:
                intervals[i][index] += "]"
            else:
                intervals[i][index] += "["
        elif array [1] == "+inf":
            intervals[i][index] = ",".join(array)+"["
            if "=" in opp:
                intervals[i][index] = "[" + intervals[i][index]
            else:
                intervals[i][index] = "]" + intervals[i][index]
        else: # no +inf nor -inf
            if "=" in opp:
                intervals[i][index] = "[" + ",".join(array) + "]"
            else:
                intervals[i][index] = "]" + ",".join(array) + "["
if ">" in opp :
    print("x E " + "U".join(intervals[1]))
else :
    print("x E " + "U".join(intervals[0]))
#test remake 1
#2794 bytes extra
#Fail
from math import sqrt
print("--------------------------------")
input1 = input("f(x) : ") 
if input1[-1] == ")":
    input1 += "=0"
if input1[-3] == ")":
    opp = input1[-2]
else :
    opp = input1[-3]+input1[-2]
fx = input1[:-2]
__opperations = fx.split(")")
__opperations.pop()
__opperations = [x[1:] for x in __opperations]
for i in range(len(__opperations)):
    p = False
    opperation_p=__opperations[i].split("x")
    if opperation_p[0] == "":
        k = "1"
    elif opperation_p[0] == "-":
        k= "-1"
    else:
        k= opperation_p[0]
    c= opperation_p[1]
    if "S" in c:
        c:list = c.split("S")
        if c[0] == "":
            c[0] = "1"
        for ii in range(len(c)):
            if "/" in c[ii]:
                c[ii] = c[ii].split("/")
                c[ii] = float(c[ii][0])/float(c[ii][1])
        c= float(c[0]) * sqrt(float(c[1]))
    elif "^" in c:
        c = c.split("^")
        for i1 in range(len(c)):
            if "/" in c[i1]:
                c[ii] = c[ii].split("/")
                c[ii] = float(c[ii][0])/float(c[ii][1])
        c = float(c[0]) ** float(c[1])
    if "/" in str(c) :
        c = c.split("/")
        c = float(c[0])/float(c[1])
    if "/" in k:
        t = k.split("/")
        if t[1][-1] == "^":
            t[1] = t[1][:-1]
            add = True
        k = str(float(t[0])/float(t[1]))
        if add:
            k = k+"^"
    if "^" in k:
        k = float(k.split("^")[0])
        p = True
    if float(k) < 0 :
        if opp == ">": opp = "<"
        elif opp == "<": opp = ">"
        elif opp == ">=": opp = "<="
        elif opp == "<=": opp = ">="
    c = float(c)/float(k)
    if p:
        if c>0 :
            print("math error")
            exit()
        c = sqrt(abs(c))
    if c >= 0:
        c = "+"+str(c)
    __opperations[i] = "x"+str(c)
    if p:
        if float(c) != 0 :
            __opperations.append("x"+str(float(c)*-1))
        else :
            __opperations.append("x+0.0")
print("-"*32)
list_inter = []
for x in __opperations:
    if float(x[1:]) != 0 :
        x = float(x[1:])*(-1)
    else:
        x = 0.0
    if x >= 0:
        list_inter.append("+"+str(x))
    else:
        list_inter.append(str(x))
list_inter_float = [float(x) for x in list_inter]
dic_map = {}
for i in range(len(__opperations)):
    dic_map[list_inter[i]] = __opperations[i]
list_inter_float.sort()
sorted_list_inter = []
for i in list_inter_float:
    if i < 0:
        sorted_list_inter.append(str(i)) 
    if i >=0 : 
        sorted_list_inter.append("+"+str(i))
list_inter = sorted_list_inter
table_head = "-inf | "+" | ".join(list_inter)+" | +inf"
if len(table_head) > 32:
    print("table is too big... can't print")
    print("intersections : "+"|".join(list_inter))
else:
    print(table_head)
    print("-"*len(table_head))
table_head_elements = list(list_inter)
table_head_elements.insert(0,"-inf")
table_head_elements.append("+inf")
dic_sign = {}
for i in list_inter:
    signs = "-"*(list_inter.index(i)+1)
    while len(signs) < len(table_head_elements)-1:
        signs += "+"
    dic_sign[dic_map[i]] = signs
list_signs = []
for i in __opperations:
    list_signs.append(dic_sign[i])
list_index = []
for i in range(len(list_signs[0])):
    list_index.append([])
    for sign_a in list_signs:
        list_index[i].append(sign_a[i])
final = []
for i in list_index:
    temp = 1
    for x in i:
        if x == "-":
            temp *= -1
    if temp == -1:
        final.append("-")
    else:
        final.append("+")
for i in __opperations:
    print("({:6}) : {}".format(i,dic_sign[i]))
print("Solution : {}".format("".join(final)))
###solve_x(table_head_elements,final,list_inter,opp)
final = list(final)
final.append(final[-1])
if opp == "=":
    print(list_inter)
    exit()
defragment = []
intervals = []
defragment.append([final[0]])
intervals.append([table_head_elements[0]])
for i in range(len(final)):
    if i == 0 :
        pass
    elif final[i] in defragment[-1]:
        defragment[-1].append(final[i])
        intervals[-1].append(table_head_elements[i])
    else:
        defragment[-1].append(final[i])
        intervals[-1].append(table_head_elements[i])
        defragment.append([])
        intervals.append([])
        defragment[-1].append(final[i])
        intervals[-1].append(table_head_elements[i])
defragment = [x[0] for x in defragment]
interval_list = []
if opp == ">" or opp == ">=":
    for d_opp_i in range(len(defragment)):
        if defragment[d_opp_i] == "+":
            list_interval = intervals[d_opp_i]
            if list_interval[0] == "-inf" or list_interval[0] == "+inf":
                temp = "]"+list_interval[0]+";"+list_interval[-1]
                if "=" in opp:
                    temp += "]"
                else:
                    temp += "["
                interval_list.append(temp)
            else:
                if "=" in opp:
                    interval_list.append("["+list_interval[0]+";"+list_interval[-1]+"]")
                else:
                    interval_list.append("]"+list_interval[0]+";"+list_interval[-1]+"[")
elif opp == "<" or opp == "<=":
    for d_opp_i in range(len(defragment)):
        if defragment[d_opp_i] == "-":
            list_interval = intervals[d_opp_i]
            if list_interval[0] == "-inf" or list_interval[0] == "+inf":
                temp = "]"+list_interval[0]+";"+list_interval[-1]
                if "=" in opp:
                    temp += "]"
                else:
                    temp += "["
                interval_list.append(temp)
            else:
                if "=" in opp:
                    interval_list.append("["+list_interval[0]+";"+list_interval[-1]+"]")
                else:
                    interval_list.append("]"+list_interval[0]+";"+list_interval[-1]+"[")
print_str = "x E " + interval_list.pop(0)
for i in interval_list:
    print_str += "U"+i
print(print_str)
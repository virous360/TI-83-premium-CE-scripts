from math import sqrt
def main():
    print("--------------------------------")
    input1 = input("f(x) : ") # (x-c1)(-x+c2)... opp 0
    if input1[-1] == ")":
        input1 += "=0"
    #extract f(x) and opperator
    if input1[-3] == ")":
        opp = input1[-2]
    else :
        opp = input1[-3]+input1[-2]
    # remove parentheses / correct opp with +x if -x 
    opperations,opp = proccess_input(input1[:-2],opp)
    tableau_de_signes(opperations,opp)

def proccess_input(fx,opp):
    # split to list of [+-x +- c ]
    opperations = fx.split(")")
    opperations.pop()
    opperations = [x[1:] for x in opperations]
    # remove -x and switch opp
    for i in range(len(opperations)):
        opperation = opperations[i]
        #reset power x^2 test
        p = False
        opperation_p=opperation.split("x")
        if opperation_p[0] == "":
            opperation_p[0] = "1"
        c = opperation_p[1]
        k = opperation_p[0]
        #c and k (check S[sqrt] or ^2)
        if "S" in c:
            c = c.split("S")
            if c[0] == "":
                c[0] = "1"
            for ii in range(len(c)):
                iii = c[ii]
                if "/" in iii:
                    iii = iii.split("/")
                    c[ii] = float(iii[0])/float(iii[1])
            c= float(c[0]) * sqrt(float(c[1]))
        elif "^" in c:
            c = c.split("^")
            for i1 in range(len(c)):
                iii = c[i1]
                if "/" in iii:
                    iii = iii.split("/")
                    c[i1] = float(iii[0])/float(iii[1])
            c = float(c[0]) ** float(c[1])
        #/ 
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

        # k^x ; ignore ^ ... c = c/k ... add opp with -c
        if "^" in k:
            k = float(k.split("^")[0])
            p = True
        # if k < 0 flip opp ... c = c/k
        if float(k) < 0 :
            opp = inv_opp(opp)
        c = float(c)/float(k)
        if p:
            if c>0 :
                print("math error")
                exit()
            c = sqrt(abs(c))
        #if c > 0 add + 
        if c >= 0:
            c = "+"+str(c)
        opperations[i] = "x"+str(c)
        if p:
            if float(c) != 0 :
                opperations.append("x"+str(float(c)*-1))
            else :
                opperations.append("x+0.0")
    return opperations,opp
def inv_opp(opp):
    if opp == ">": opp = "<"
    elif opp == "<": opp = ">"
    elif opp == ">=": opp = "<="
    elif opp == "<=": opp = ">="
    return opp
def tableau_de_signes(opperations:list,opp):
    print("-"*32)
    # get the intersections for each intersection
    list_inter = []
    for x in opperations:
        # exeption x = -0
        if float(x[1:]) != 0 :
            x = float(x[1:])*(-1)
        # if ("+"+str(x) in list_inter) or (str(x) in list_inter):
        #     pass
        else:
            x = 0.0
        if x >= 0:
            list_inter.append("+"+str(x))
        else:
            list_inter.append(str(x))
    list_inter_float = [float(x) for x in list_inter]
    # create map 
    dic_map = {}
    for i in range(len(opperations)):
        dic_map[list_inter[i]] = opperations[i]
    #sort intersections 
    list_inter_float.sort()
    sorted_list_inter = []
    for i in list_inter_float:
        if i < 0:
            sorted_list_inter.append(str(i)) 
        if i >=0 : 
            sorted_list_inter.append("+"+str(i))
    list_inter = sorted_list_inter
    #print table head
    table_head = "-inf | "+" | ".join(list_inter)+" | +inf"
    if len(table_head) > 32:
        print("table is too big... can't print")
        print("intersections : "+"|".join(list_inter))
    else:
        print(table_head)
        print("-"*len(table_head))
    # list of elements
    table_head_elements = list(list_inter)
    table_head_elements.insert(0,"-inf")
    table_head_elements.append("+inf")
    # dic containing the sign and opperation 
    dic_sign = {}
    for i in list_inter:
        signs = "-"*(list_inter.index(i)+1)
        while len(signs) < len(table_head_elements)-1:
            signs += "+"
        dic_sign[dic_map[i]] = signs
    # list of all signs
    list_signs = []
    for i in opperations:
        list_signs.append(dic_sign[i])
    # result 
    final = multiply_signs(list_signs)
    #print
    for i in opperations:
        print("({:6}) : {}".format(i,dic_sign[i]))
    print("Solution : {}".format("".join(final)))
    solve_x(table_head_elements,final,list_inter,opp)
def multiply_signs(list_signs:list[str]):
    #get list by column instead of rows
    list_index = []
    for i in range(len(list_signs[0])):
        list_index.append([])
        for sign_a in list_signs:
            list_index[i].append(sign_a[i])
    # make a calc of each index
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
    return final    
def solve_x(table_head_elements,final,list_inter,opp):
    final = list(final)
    # final.insert(0,final[0])
    final.append(final[-1])
    if opp == "=":
        print(list_inter)
        return
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
    #A5IRAN
    print_str = "x E " + interval_list.pop(0)
    for i in interval_list:
        print_str += "U"+i
    print(print_str)

main()
""" Fonctions : Tableau de signes et variation
Cree par: Ali Naim
Date : 10/12/2022
version : 1.0
len screen :32"""
def main():
    print("--------------------------------")
    input1 = input("f(x) : ") # (x-c1)(-x+c2)... opp 0
    #extract f(x) and opperator
    if input1[-3] == ")":
        opp = input1[-2]
    else :
        opp = input1[-3]+input1[-2]
    fx = input1[:-2]
    # remove parentheses / correct opp with +x if -x 
    opperations,opp = proccess_input(fx,opp)
    tableau_de_signes(opperations,opp)

def proccess_input(fx:str,opp:str):
    # split to list of [+-x +- c ]
    opperations = fx.split(")")
    opperations.pop()
    opperations = [x[1:] for x in opperations]\
    # remove -x and switch opp
    for opperation in opperations:
        if opperation[0] != "x": #-x
            # c * -1
            c = float(opperation[2:]) * (-1)
            #reassign
            if c >= 0:
                opperations[opperations.index(opperation)] = "x+"+str(c)
            else:
                opperations[opperations.index(opperation)] = "x"+str(c)
            #change opp
            if opp == ">": opp = "<"
            elif opp == "<": opp = ">"
            elif opp == ">=": opp = "<="
            elif opp == "<=": opp = ">="
    return opperations,opp

def tableau_de_signes(opperations:list,opp:str):
    print("-"*32)
    # get the intersections for each intersection
    list_inter = []
    for x in opperations:
        x = float(x[1:])*(-1)
        # if ("+"+str(x) in list_inter) or (str(x) in list_inter):
        #     pass
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
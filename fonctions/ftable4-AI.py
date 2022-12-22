# 3.0
from math import sqrt
opp = None
def main():
    global opp
    print("--------------------------------")
    input1 = input("f(x) : ") 
    if input1[-1] == ")":
        input1 += "=0"
    if input1[-3] == ")":
        opp = input1[-2]
    else:
        opp = input1[-3]+input1[-2]
    terms, opp = process_input(input1[:-2], opp)
    tableau_de_signes(terms, opp)

def tableau_de_signes(terms, opp):
    print("-"*32)
    dic_map = {str(float(x.split("x")[1]) * -1): terms[i] for i, x in enumerate(terms) if float(x.split("x")[1]) != 0}
    dic_map = {("+" + x if float(x) >= 0 else x): terms[i] for i, x in enumerate(dic_map)}
    list_inter_float = (float(x) for x in dic_map.keys())
    list_inter_float = sorted(list_inter_float)
    sorted_list_inter = ["+" + str(i) if i >= 0 else str(i) for i in list_inter_float]
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
    list_signs = [dic_sign[i] for i in terms]
    list_signs = []
    for i in terms:
        list_signs.append(dic_sign[i])
    final = multiply_signs(list_signs)
    for i in terms:
        print("({:6}) : {}".format(i,dic_sign[i]))
    print("Solution : {}".format("".join(final)))
    solve_x(table_head_elements,final,list_inter,opp)


def multiply_signs(list_signs):
    list_index = ((sign_a[i] for sign_a in list_signs) for i in range(len(list_signs[0])))
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

def process_input(fx, opp):
    fx = fx.split(")")
    fx.pop()
    terms = [x[1:] for x in fx]
    terms = [proccess_term(x) for x in terms]
    return terms, opp

def div(c):
    if "/" in c:
        numerator, denominator = c.split("/")
        return float(numerator) / float(denominator)
    return float(c)

def proccess_term(x):
    p = False
    x = x.split("x")
    if x[0] == "":
        k = "1"
    elif x[0] == "-":
        k = "-1"
    else:
        k = x[0]
    c = x[1]
    if "S" in c:
        c = c.split("S")
        if c[0] == "":
            c[0] = "1"
        for ii in range(len(c)):
            if "/" in c[ii]:
                c[ii] = div(c[ii])
        c = float(c[0]) * sqrt(float(c[1]))
    elif "^" in c:
        c = c.split("^")
        for i1 in range(len(c)):
            if "/" in c[i1]:
                c[i1] = div(c[i1])
        c = float(c[0]) ** float(c[1])
    if "/" in str(c):
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
    return "x"+str(c)

def solve_x(table_head_elements, final, list_inter, opp):
    final = list(final)
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
    print_str = "x E " + interval_list.pop(0)
    for i in interval_list:
        print_str += "U"+i
    print(print_str)


main()
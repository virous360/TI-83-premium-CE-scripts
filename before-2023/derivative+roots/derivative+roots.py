# table of variation 
#https://calcworkshop.com/derivatives/power-rule/
import math
##proccess input
print("-"*32)
# fx = input("f(x) : ") 
fx = "x^4+3x^3-x^2-2x+2"  #"4x^3+9x^2-2x-2"
fx = fx.replace("X","x")
fx_query = [[],[],[],[],[],[]]
fx = fx.split("+")
newfx = []
for i in fx:
    if "-" in i:
        i = i.split("-")
        newfx.append(i[0])
        for index2,i2 in enumerate(i):
            if index2 != 0:
                newfx.append("-"+i2)
    else:
        newfx.append(i)
fx = [[],[],[],[],[]] # powers : 0 1 2 3 4 
for index,i in enumerate(newfx):
    i = i.split("x")
    if len(i) == 1:
        fx_query[0] = i[0]
        break
    i[1] = i[1][1:]
    if i[0] == "":
        i[0] = "1"
    elif i[0] == "-":
        i[0] = "-1"
    if i[1] == "":
        i[1] = "1"
    fx_query[int(i[1])] = i[0]
    i[0] = float(i[0]) * float(i[1])
    i[1] = float(i[1])-1
    fx[int(i[1])] = i[0]

for index,i in enumerate(fx):
    if i == []:
        fx.pop(index)
for index,i in enumerate(fx_query):
    if i == []:
        fx_query.pop(index)
fx.reverse()
degree = len(fx)-1
## find roots
def find_roots_4(coeffs):
    #ax^4 + bx^3 + cx^2 + dx + e = 0
    a, b, c, d, e = coeffs
    roots = [0, 0, 0, 0]
    # Case 1: all roots are real
    if b**2 - 4*a*c >= 0 and d**2 - 4*b*e >= 0:
        roots[0] = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        roots[1] = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        roots[2] = (-d + math.sqrt(d**2 - 4*b*e)) / (2*b)
        roots[3] = (-d - math.sqrt(d**2 - 4*b*e)) / (2*b)
    # Case 2: two roots are real, two are complex
    elif b**2 - 4*a*c < 0 and d**2 - 4*b*e >= 0:
        roots[0] = (-b + 1j*math.sqrt(4*a*c - b**2)) / (2*a)
        roots[1] = (-b - 1j*math.sqrt(4*a*c - b**2)) / (2*a)
        roots[2] = (-d + math.sqrt(d**2 - 4*b*e)) / (2*b)
        roots[3] = (-d - math.sqrt(d**2 - 4*b*e)) / (2*b)
    # Case 3: two roots are real, two are complex
    elif b**2 - 4*a*c >= 0 and d**2 - 4*b*e < 0:
        roots[0] = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        roots[1] = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        roots[2] = (-d + 1j*math.sqrt(4*b*e - d**2)) / (2*b)
        roots[3] = (-d - 1j*math.sqrt(4*b*e - d**2)) / (2*b)
    # Case 4: all roots are complex
    else:
        roots[0] = (-b + 1j*math.sqrt(4*a*c - b**2)) / (2*a)
        roots[1] = (-b - 1j*math.sqrt(4*a*c - b**2)) / (2*a)
        roots[2] = (-d + 1j*math.sqrt(4*b*e - d**2)) / (2*b)
        roots[3] = (-d - 1j*math.sqrt(4*b*e - d**2)) / (2*b)
    return roots
def find_roots_3(coeffs):
    a, b, c, d = coeffs
    roots = [0, 0, 0]
    
    # Use the Cardano formula to find the roots
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    disc = q**2 + 4*p**3 / 27
    
    # Case 1: one real root and two complex roots
    if disc > 0:
        u1 = (-q + math.sqrt(disc)) / 2
        u2 = (-q - math.sqrt(disc)) / 2
        v1 = u1**(1/3)
        v2 = u2**(1/3)
        roots[0] = v1 + v2 - b / (3*a)
        roots[1] = (-v1 - v2 - b / (3*a)) / 2 + 1j*math.sqrt(3)/2*(v1 - v2)
        roots[2] = (-v1 - v2 - b / (3*a)) / 2 - 1j*math.sqrt(3)/2*(v1 - v2)
    # Case 2: all roots are real
    elif disc == 0:
        u = -q / 2
        v = u**(1/3)
        roots[0] = 2*v - b / (3*a)
        roots[1] = -v - b / (3*a)
        roots[2] = -v - b / (3*a)
    # Case 3: one real root and two complex roots
    else:
        u = -q / 2
        v = math.sqrt(-p / 3)
        theta = math.acos(-q / (2*math.sqrt(-p**3 / 27)))
        roots[0] = 2*v*math.cos(theta/3) - b / (3*a)
        roots[1] = 2*v*math.cos((theta + 2*math.pi)/3) - b / (3*a)
        roots[2] = 2*v*math.cos((theta + 4*math.pi)/3) - b / (3*a)
    
    return roots
def find_roots_2(coeffs):
    a, b, c = coeffs
    roots = [0, 0]
    
    # Use the quadratic formula to find the roots
    disc = b**2 - 4*a*c
    if disc < 0:
        # All roots are complex
        roots[0] = (-b + 1j*math.sqrt(-disc)) / (2*a)
        roots[1] = (-b - 1j*math.sqrt(-disc)) / (2*a)
    else:
        # All roots are real
        roots[0] = (-b + math.sqrt(disc)) / (2*a)
        roots[1] = (-b - math.sqrt(disc)) / (2*a)
    
    return roots
def find_roots_1(coeffs):
    a, b = coeffs
    root = 0
    
    # Find the root
    root = -b / a
    
    return root

if degree == 4:
    roots = find_roots_4(fx)
elif degree == 3:
    roots =  find_roots_3(fx)
elif degree == 2:
    roots = find_roots_2(fx)
elif degree == 1 :
    roots = find_roots_1(fx)
else:
    print("error")
    exit()

#find deriavtive function 
fx.reverse()
for index, value in enumerate(fx):
    if float(value).is_integer():
        value = int(value)
    if value >=0:
        value = "+" + str(value)
    if index != 0 and index != 1 :
        fx[index] = str(value) +  "x^" + str(index)
    elif index == 1:
        fx[1] = str(value) + "x"
    else:
        fx[0] = str(value)
fx.reverse()
if fx[0][0] == "+":
    fx[0] = fx[0][1:]
print("f'(X) = "+"".join(fx))
roots.sort()
roots = [str(round(x,3)) for x in roots]
print("roots : "+" , ".join(roots))

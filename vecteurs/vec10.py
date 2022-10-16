'''python 3.10 Vecteurs 
Ali Naim ;16/10/2022
'''
import math
from sys import exit

def error (i : int):
    print("error code " + str(i))
    exit()
def opp(i: float):
    """get the opposite of a value

    Args:
        i (float|int): number to be inversed

    Returns:
        float: positve num ? negative num , positif num;
    """     
    return i * (-1)
# work in (o,x'x,y'y)s
class vector2:
    """defines a vector class with coords (x,y) , direction , sense , lenght
    with functions :
        constuctor,get_coords,inverse

    Returns:
        null: null
    """
    # coords
    x = 0
    y = 0
    # calculate direction as angle from (origin, oy) 
    direction = 0   # from -90 to 90 deg. 
    sense = {
        "up" : False,
        "down" : False,
        "left" : False,
        "right" : False
    }
    norme = 0 # lenght 
    def dumpp(self):
        print("=================================")
        print("coords :",self.get_coords())
        print("direction (en deg.) =",self.direction)
        print("sense :",self.sense)
        print("norme = ", self.norme)
        print("=================================")
    def __update_sense(self):
        """private method to update the sense of the vector 
        """
        self.sense = {
        "up" : False,
        "down" : False,
        "left" : False,
        "right" : False
        }
        # sense 
        if self.y >0:
            self.sense["up"] = True
        elif self.y < 0: 
            self.sense["down"] = True
        if self.x > 0:
            self.sense["right"] = True        
        elif self.x < 0 : 
            self.sense["left"] = True
    def __init__(self,x: float,y: float):
        """initial constructor

        Args:
            x (float | int): x coord of the vector 
            y (float | int): y coord of the vector 
        """
        self.x = x
        self.y  = y
        # direction = tan^-1(alpha) ;    tan(alpha) = y / x 
        if x != 0:
            self.direction = math.degrees(math.atan(self.y/self.x))
        self.__update_sense()
        self.norme = math.sqrt(x**2 + y**2)
    def get_coords(self):
        """easy way to get x and y of a vec.

        Returns:
            tuple: (x,y)
        """
        return (self.x, self.y)
    def inverse (self):
        """get the opp of a vector without messing up the sense
        """
        self.x = opp(self.x)
        self.y = opp(self.y)
        self.__update_sense()
class point:
    """define a point 
    """
    x = 0
    y = 0
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y    
    def get_coords (self): 
        return (self.x , self.y)
def ABvector(st: point,ex: point):
    v_x = ex.x - st.x
    v_y = ex.y - st.y
    vec = vector2(v_x,v_y)
    return vec
def add_vect(A: vector2 , B: vector2):
    x = A.x + B.x
    y = A.y + B.y
    v = vector2(x,y)
    return v
def sub_vect(A : vector2, B : vector2):
    B.inverse()
    v = add_vect(A,B)
    return v
def det(A: vector2, B : vector2):
    eq = A.x * B.y - A.y * B.x
    return eq
def iscollinear(A: vector2, B : vector2):
    eq = det(A,B)
    if eq == 0 :
        return True
    else :
        return False 
def iscenterofgravity(a : point , b : point , c : point , g : point):
    ga_v = ABvector(g,a)
    gb_v = ABvector(g,b)
    gc_v = ABvector(g,c)
    eq = add_vect(add_vect(ga_v,gb_v), gc_v)
    if eq.get_coords() == (0,0):
        return True
    else :
        return False
def getcenterofgravity(a : point , b : point , c : point):
    x = (a.x + b.x + c.x)/ 3
    y = (a.y + b.y + c.y)/ 3
def get_extermity (v : vector2,st : point):
    # v_x + A.x= etrem 
    x = v.x + st.x
    y = v.y + st.y
    p = point(x,y)
    return p
def get_origin(v : vector2, ext : point):
    x = ext.x - v.x
    y = ext.y - v.y
    p = point(x,y)
    return p
def points_colinear_three(point1: point , point2 : point , point3: point):
    o = point1
    a = point2 
    b = point3
    v1 = ABvector(o,a)
    v2 = ABvector(o,b)
    return iscollinear(v1, v2)

# Main
'''options :
det    
collinear?
3 points collinear
    is center of gravity?
    get center og gravity
get_extr
get origin
'''
while(True):
    menu = input("""1. calcule vecteurs
2. det/collinear
3. center of gravity
4. get extremity/ origin
:""")
    try:
        menu = int(menu)
    except:
        error(0)
    if menu <= 0 or menu >4:
        error(1)
    if menu == 1:
        inp = input("""1. ABvector
2. vecteur(x,y)
3. add
4. sub
:""")
        try:
            inp = int(inp)
        except:
            error(1)
        if inp <= 0 or inp > 4 :
            error(2)
        if inp == 1 : #ABvector
            print("sois le vecteur ab->")
            x1 = float(input("x de a : "))
            y1 = float(input("y de a : "))
            x2 = float(input("x de b : "))
            y2 = float(input("y de b : "))
            p1 = point(x1,y1)
            p2 = point(x2, y2)
            ABvector(p1,p2).dumpp()
        elif inp == 2  : #vecteur(x,y)
            print("ab-> (x,y)")
            x = float(input("x = "))
            y = float(input("y = "))
            v = vector2(x,y)
            v.dumpp()
        elif inp == 3: #add
            print("v1 (x1,y1) and v2 (x2,y2)")
            x1 = float(input("x1 = "))
            y1 = float(input("y1 = "))
            x2 = float(input("x2 = "))
            y2 = float(input("y2 = "))
            v1 = vector2(x1,y2)
            v2 = vector2(x2,y2)
            v3 = add_vect(v1,v2)
            v3.dumpp()
        elif inp ==4 : #sub
            pass
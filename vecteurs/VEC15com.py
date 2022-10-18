import math;from sys import exit
def e(i):
 print("error code " + str(i));exit()
class vector2:
 x=0;y=0;dir=0;sense={"up":False,"down":False,"left" :False,"right":False};norme=0
 def dumpp(self):
  print("===============================")
  print("coords :",self.get_coords())
  print("direction (en deg.) =",self.dir)
  print("sense :",self.sense)
  print("norme = ", self.norme)
  print("===============================")
 def __update_sense(self):
  self.sense={"up":False,"down":False,"left":False,"right":False}
  if self.y>0:
   self.sense["up"] = True
  elif self.y<0: 
   self.sense["down"] = True
  if self.x>0:
   self.sense["right"] = True
  elif self.x<0: 
   self.sense["left"] = True
 def __init__(self,x,y):
  self.x=x;self.y=y
  if x!=0:
   self.dir=round(math.degrees(math.atan(self.y/self.x)),2);self.__update_sense();self.norme=round(math.sqrt(x**2 + y**2),4)
 def get_coords(self):
  return (self.x, self.y)
 def inverse (self):
  self.x=self.x*-1;self.y=self.y*-1;self.__update_sense()
class point:
 x=0;y=0
 def __init__(self,x,y):
  self.x=x;self.y=y    
 def get_coords(self): 
  return (self.x,self.y)
def ABvector(st,ex):
 v_x=ex.x-st.x;v_y=ex.y-st.y;vec=vector2(v_x,v_y);return vec
def add_vect(A,B):
 x=A.x+B.x;y=A.y+B.y;v=vector2(x,y);return v
def sub_vect(A,B):
 B.inverse();v=add_vect(A,B);return v
def det(A,B):
 return A.x*B.y-A.y*B.x
def iscollinear(A,B):
 if det(A,B)==0:
  return True
 else:
  return False 
def iscenterofgravity(a,b,c,g):
 if add_vect(add_vect(ABvector(g,a),ABvector(g,b)), ABvector(g,c)).get_coords() == (0,0):
  return True
 else :
  return False
def getcenterofgravity(a,b,c):
 return point((a.x + b.x + c.x)/ 3,(a.y + b.y + c.y)/ 3)
def get_extermity (v,st):
 return point(v.x+st.x,v.y+st.y)
def get_origin(v,ext):
 return point(ext.x-v.x,ext.y-v.y)
def points_colinear_three(o,a,b):
 return iscollinear(ABvector(o,a),ABvector(o,b))
def getv1(num):
 vl = []
 for i in range(1,num+1):
  print("v"+str(i)+" = (x,y)")
  vl.append(vector2(float(input("x = ")),float(input("y = "))))
 return vl
def getpoint(i):
 x = float(input("x"+str(i)+" ="))
 y = float(input("y"+str(i)+" ="))
 p = point(x,y)
 return p
# Main

menu = input("""1. calcule vecteurs
2. det/collinear
3. center of gravity
4. get extremity/ origin
:""")
try:
 menu = int(menu)
except:
 e(0)
if menu <= 0 or menu >4:
 e(1)
if menu == 1:
 inp = input("""1. ABvector
2. vecteur(x,y)
3. add
4. sub
:""")
 try:
  inp = int(inp)
 except:
  e(0)
 if inp <= 0 or inp > 4 :
  e(2)
 if inp == 1 :
  print("sois le vecteur ab->")
  p1 = getpoint(1)
  p2 = getpoint(2)
  ABvector(p1,p2).dumpp()
 elif inp == 2  : 
  print("ab-> (x,y)")
  x = float(input("x = "))
  y = float(input("y = "))
  v = vector2(x,y)
  v.dumpp()
 elif inp == 3:
  l = getv1(2)
  v3 = add_vect(l[0],l[1])
  v3.dumpp()
 elif inp ==4 : #sub
  l = getv1(2)
  v3 = sub_vect(l[0],l[1])
  v3.dumpp()
elif menu == 2: #det/collinear
 inp = input("""1. det(v1,v2)
2. colinear (v1,v2)
3. 3 points colinear""")
 try:
  inp = int(inp)
 except:
  e(0)
 if inp <= 0 or inp > 3 :
  e(3)
 if inp == 1:
  l = getv1(2)
  print("det(v1,v2) =",det(l[0],l[1]))
 elif inp==2:#colin
  l = getv1(2)
  print(iscollinear(l[0],l[1]))
 elif inp==3:#3points colin
  p1 = getpoint(1)
  p2 = getpoint(2)
  p3 = getpoint(3)
  print(points_colinear_three(p1,p2,p3))
elif menu == 3: #center of gravity
 inp = """1. is center of gravity
2. find center of gravity"""
 if inp == 1:
  print("les point 1,2,3 ext. du tri. et 4 centre a tester")
  p1 = getpoint(1)
  p2 = getpoint(2)
  p3 = getpoint(3)
  p4 = getpoint(4)
  print(iscenterofgravity(p1,p2,p3,p4))
 elif inp == 2:
  print("les point 1,2,3 ext. du tri.")
  p1 = getpoint(1)
  p2 = getpoint(2)
  p3 = getpoint(3)
  print(getcenterofgravity(p1,p2,p3).get_coords())
elif menu == 4: #get extremity/ origin
 inp = int(input("""1.get origin
2.get ext.
:"""))
 if inp == 1 :
  print("ext:")
  v1 = getv1(1)
  p1 = getpoint(1)
  print(get_origin(v1[0],p1))
 elif inp ==2:
  print("origin:")
  v1 = getv1(1)
  p1 = getpoint(1)
  print(get_extermity(v1[0],p1))
import math as m;from sys import exit
class v2:
 def vf1(self):print("===============================\ncoords :",self.vf3(),"\ndirection (en deg.) =",self.dir,"\nsense :",self.sense,"\nnorme = ",self.norme,"\n===============================")
 def vf2(self):
  self.sense={"up":False,"down":False,"left":False,"right":False}
  if self.y>0:self.sense["up"]=True
  elif self.y<0:self.sense["down"]=True
  if self.x>0:self.sense["right"]=True
  elif self.x<0:self.sense["left"]=True
 def __init__(self,x,y):
  self.x=x;self.y=y
  if x!=0:self.dir=round(m.degrees(m.atan(y/x)),2)
  else:self.dir="cant divide by 0"
  self.vf2();self.norme=round(m.sqrt(x**2 + y**2),4)
 def vf3(self):
  return(self.x, self.y)
 def inverse(self):
  self.x=self.x*-1;self.y=self.y*-1;self.vf2()
class point:
 def __init__(self,x,y):
  self.x=x;self.y=y    
 def vf3(self):return (self.x,self.y)
def f2(A,B):return v2(A.x+B.x,A.y+B.y)
def f3(A,B):B.inverse();return f2(A,B)
def iscollinear(A,B):
 if A.x*B.y-A.y*B.x==0:return True
 else:return False 
def iscenterofgravity(a,b,c,g):
 if f2(f2(v2(a.x-g.x,a.y-g.y),v2(b.x-g.x,b.y-g.y)), v2(c.x-g.x,c.y-g.y)).vf3() == (0,0):
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
 return iscollinear(v2(a.x-o.x,a.y-o.y),v2(b.x-o.x,b.y-o.y))
def getv1(num):
 vl = []
 for i in range(1,num+1):
  print("v"+str(i)+" = (x,y)")
  vl.append(v2(float(input("x = ")),float(input("y = "))))
 return vl
def getpoint(i):
 x = float(input("x"+str(i)+" ="))
 y = float(input("y"+str(i)+" ="))
 p = point(x,y)
 return p
# Main

menu = int(input("""1. calcule vecteurs
2. det/collinear
3. center of gravity
4. get extremity/ origin
:"""))
if menu == 1:
 inp = int(input("""1. AB vecteur
2. vecteur(x,y)
3. add
4. sub
:"""))
 if inp == 1 :
  print("sois le vecteur ab->")
  p1 = getpoint(1)
  p2 = getpoint(2)
  v2(p2.x-p1.x,p2.y-p1.y).vf1()
 elif inp == 2  : 
  print("ab-> (x,y)")
  x = float(input("x = "))
  y = float(input("y = "))
  v = v2(x,y)
  v.vf1()
 elif inp == 3:
  l = getv1(2)
  v3 = f2(l[0],l[1])
  v3.vf1()
 elif inp ==4 : #sub
  l = getv1(2)
  v3 = f3(l[0],l[1])
  v3.vf1()
elif menu == 2: #det/collinear
 inp = int(input("""1. det(v1,v2)
2. colinear (v1,v2)
3. 3 points colinear
:"""))
 if inp == 1:
  l = getv1(2)
  print("det(v1,v2) =",l[0].x*l[1].y-l[0].y*l[1].x)
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
2. find center of gravity
:"""
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
  print(getcenterofgravity(p1,p2,p3).vf3())
elif menu == 4: #get extremity/ origin
 inp = int(input("""1.get origin
2.get ext.
:"""))
 if inp == 1 :
  print("ext:")
  v1 = getv1(1)
  p1 = getpoint(1)
  print(get_origin(v1[0],p1).vf3())
 elif inp ==2:
  print("origin:")
  v1 = getv1(1)
  p1 = getpoint(1)
  print(get_extermity(v1[0],p1).vf3())
# Main
 ,"\nsense :",self.sense,"\nnorme = ",self.norme,"\n===============================")





if A1:
vecteur2(l[1].x-l[0].x,l[1].y-l[0].y).dumpp()
elif A2:
getv1(1)[0].dumpp()
elif A3:
l=getv1(2);add_vectors(l[0],l[1]).dumpp()
elif A4:
l=getv1(2);sub_vecteurs(l[0],l[1]).dumpp()





elif menu==2:
 inp = int(input("""1. det(v1,vecteur2)
2. colinear (v1,vecteur2)
3. 3 points colinear
:"""))
 if inp==1:l=getv1(2);print("det(v1,vecteur2) =",l[0].x*l[1].y-l[0].y*l[1].x)
 elif inp==2:l=getv1(2);print(iscollinear(l[0],l[1]))
 elif inp==3:l=getpoint(3);print(points_colinear_three(l[0],l[1],l[2]))
elif menu==3:
 inp="""1. is center of gravity
2. find center of gravity
:"""
 if inp==1:print("les points 1,2,3 ext. du tri. et 4 centre a teste");l=getpoint(4);print(iscenterofgravity(l[0],l[1],l[2],l[3]))
 elif inp==2:print("les point 1,2,3 ext. du tri.");l=getpoint(3);print(getcenterofgravity(l[0],l[1],l[2]).coords_vecteur())
elif menu==4:
 inp = int(input("""1.get origin
2.get ext.
:"""))
 if inp==1:print("ext:\n",get_origin(getv1(1)[0],getpoint(1)[0]).coords_vecteur())
 elif inp==2:print("origin:\n",get_extermity(getv1(1)[0],getpoint(1)[0]).coords_vecteur())

















import math as m
class vecteur2:
 def update_sense(self):
  self.sense={"up":False,"down":False,"left":False,"right":False}
  if self.y>0:self.sense["up"]=True
  elif self.y<0:self.sense["down"]=True
  if self.x>0:self.sense["right"]=True
  elif self.x<0:self.sense["left"]=True
 def __init__(self,x,y):
  self.x=x;self.y=y
  if x!=0:self.dir=round(m.degrees(m.atan(y/x)),2)
  else:self.dir="cant divide by 0"
  self.update_sense();self.norme=round(m.sqrt(x**2 + y**2),4)
 def coords_vecteur(self):
  return(self.x, self.y)
 def inverse(self):
  self.x=self.x*-1;self.y=self.y*-1;self.update_sense()
class point:
 def __init__(self,x,y):
  self.x=x;self.y=y    
 def coords_vecteur(self):return (self.x,self.y)
def add_vectors(A,B):return vecteur2(A.x+B.x,A.y+B.y)
def sub_vecteurs(A,B):B.inverse();return add_vectors(A,B)
def iscollinear(A,B):
 if A.x*B.y-A.y*B.x==0:return True
 else:return False 
def iscenterofgravity(a,b,c,g):
 if add_vectors(add_vectors(vecteur2(a.x-g.x,a.y-g.y),vecteur2(b.x-g.x,b.y-g.y)), vecteur2(c.x-g.x,c.y-g.y)).coords_vecteur()==(0,0):return True
 else:return False
def getcenterofgravity(a,b,c):return point((a.x + b.x + c.x)/ 3,(a.y + b.y + c.y)/ 3)
def get_extermity(v,st):return point(v.x+st.x,v.y+st.y)
def get_origin(v,ext):return point(ext.x-v.x,ext.y-v.y)
def points_colinear_three(o,a,b):return iscollinear(vecteur2(a.x-o.x,a.y-o.y),vecteur2(b.x-o.x,b.y-o.y))
def getv1(num):return[vecteur2(float(input("x de v"+str(i)+" = ")),float(input("y de v"+str(i)+" = "))) for i in range(1,num+1)]
def getpoint(num):return[point(float(input("x"+str(i)+" =")),float(input("y"+str(i)+" ="))) for i in range(1,num+1)]

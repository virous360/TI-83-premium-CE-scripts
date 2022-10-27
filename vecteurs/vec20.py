from math import sqrt,degrees,atan
def round(f:float,n:int):
   return str(int(f))+str(f-int(f))[:n+1][1:]
def v2(x:float,y:float):
   if x!=0:dir=round(degrees(atan(y/x)),2)
   else:dir="cant divide by 0"
   sense={"up":False,"down":False,"left":False,"right":False}
   if y>0:sense["up"]=True
   elif y<0:sense["down"]=True
   if x>0:sense["right"]=True
   elif x<0:sense["left"]=True
   print("===============================\ncoords :",(round(x,2),round(y,2)),"\ndirection (en deg.) =",dir,"\nsense :",sense,"\nnorme = ",round(sqrt(x**2 +y**2),4),"\n===============================")
def add_vec(A:list[float],B:list[float]):return[A[0]+B[0],A[1]+B[1]]
def sub_vec(A:list[float],B:list[float]):B[0]=B[0]*-1;B[1]=B[1]*-1;return add_vec(A,B)
def is_collinear(A:list[float],B:list[float]):
 if A[0]*B[1]-A[1]*B[0]==0:return True
 else:return False
def is_center_of_gravity(a:list[float],b:list[float],c:list[float],g:list[float]):
 if add_vec(add_vec([a[0]-g[0],a[1]-g[1]],[b[0]-g[0],b[1]-g[1]]),[c[0]-g[0],c[1]-g[1]])==[0,0]:return True
 else:return False
def get_center_of_gravity(a:list[float],b:list[float],c:list[float]):return[(a[0]+b[0]+c[0])/3,(a[1]+b[1]+c[1])/3]
def points_colinear_three(o:list[float],a:list[float],b:list[float]):return is_collinear([a[0]-o[0],a[1]-o[1]],[b[0]-o[0],b[1]-o[1]])
def get_vectors(num:int):return[[float(input("x de v"+str(i)+" = ")),float(input("y de v"+str(i)+" = "))] for i in range(1,num+1)]
def get_points(num):return[[float(input("x"+str(i)+" =")),float(input("y"+str(i)+" ="))] for i in range(1,num+1)]
menu=int(input("1. calcule vecteurs\n2. det/collinear\n3. center of gravity\n4. get extremity/ origin\n5. orthogonal\n:"))
if menu==1:
 inp=int(input("""1. AB vecteur\n2. vecteur(x,y)\n3. add\n4. sub\n:"""))
 if inp==1:
    print("sois le vecteur ab->")
    l = get_points(2)
    v2(l[1][0]-l[0][0],l[1][1]-l[0][1])
 elif inp==2:l=get_vectors(1)[0];v2(l[0],l[1])
 elif inp==3 or inp==4:
   l=get_vectors(2)
   if inp==3:b=add_vec(l[0],l[1])
   else:b=sub_vec(l[0],l[1])
   v2(b[0],b[1])
elif menu==2:
 inp=int(input("1. det(v1,v2)\n2. colinear (v1,v2)\n3. 3 points colinear\n:"))
 if inp==1:l=get_vectors(2);print("det(v1,v2) =",round(l[0][0]*l[1][1]-l[0][1]*l[1][0],3))
 elif inp==2:l=get_vectors(2);print(is_collinear(l[0],l[1]))
 elif inp==3:l=get_points(3);print(points_colinear_three(l[0],l[1],l[2]))
elif menu==3:
 inp=int(input("1. is center of gravity\n2. find center of gravity\n:"))
 if inp==1:print("les points 1,2,3 ext. du tri. et 4 centre a teste");l=get_points(4);print(is_center_of_gravity(l[0],l[1],l[2],l[3]))
 elif inp==2:print("les point 1,2,3 ext. du tri.");l=get_points(3);p=get_center_of_gravity(l[0],l[1],l[2]);print([round(p[0],3),round(p[1],3)])
elif menu==4:
 inp=int(input("1. get origin\n2. get ext.\n:"))
 if inp==1 or inp==2:
   v=get_vectors(1)[0]
   p=get_points(1)[0]
   if inp==1:o=[p[0]-v[0],p[1]-v[1]];print("origin:\n",[o[0],o[1]])
   else:o=[v[0]+p[0],v[1]+p[1]];print("ext:\n",[o[0],o[1]])
elif menu==5:
   l=get_vectors(2)
   if l[0][0]*l[1][0]+l[0][1]*l[1][1]==0:print(True)
   else:print(False)

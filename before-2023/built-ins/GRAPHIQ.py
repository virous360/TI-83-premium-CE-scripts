import ti_plotlib as plt
#Après avoir exécuté ce script, appuyez sur [annul] pour effacer l'écran

def f(x):
  return 3*x**2-.4

def g(x):
  return -f(x)

def plot(res,xmin,xmax):
  #configurer l'écran graphique
  plt.window(xmin,xmax,xmin/1.5,xmax/1.5)
  plt.cls()
  gscale=5
  plt.grid((plt.xmax-plt.xmin)/gscale*(3/4),(plt.ymax-plt.ymin)/gscale,"dash")
  plt.pen("thin","solid")
  plt.color(0,0,0)
  plt.axes("on")
  plt.labels("abscisse","       ordonnee",6,1)
  plt.pen("medium","solid")

  # représenter les fonctions   f(x) et g(x)
  dX=(plt.xmax -plt.xmin)/res
  x=plt.xmin 
  x0=x
  for i in range(res):
    plt.color(255,0,0)
    plt.line(x0,f(x0),x,f(x),"")
    plt.color(0,0,255)
    plt.plot(x,g(x),"o")
    x0=x
    x+=dX
  plt.show_plot()

#plot(résolution,xmin,xmax)
plot(30,-1,1)
# Créer une graphique avec les paramètres (résolution,xmin,xmax)
# Après avoir effacé le premier graphique, appuyez sur la touche [var]. La fonction plot() permet de modifier les paramètres d’affichage (résolution,xmin,xmax).
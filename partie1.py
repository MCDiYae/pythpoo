class Vecteur2D:
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
   #l'affichage
   def display(self):
      print(self.x ,self.y)
   #addition de 2 vect
   def __add__(self,autre):
     return Vecteur2D(self.x+autre.x,self.y+autre.y)

#creation des instances 
#non paramatre
c1= Vecteur2D(2,8)
# paramatre
c2=Vecteur2D(2,1)
#affichage
c1.display()
c2.display()
s=c1+c2
s.display()




# class piont 
class Point:                 
    
    def __init__(self, x=0.0, y=0.0):    
        self.px = float(x)                       
        self.py = float(y)

class Segment:   

   
    def __init__(self, x1, y1, x2, y2):
        #"Le constructeur utilise deux instances DE CLASS POINT
        self.orig = Point(x1, y1)               
        self.extrem = Point(x2, y2)

    def __str__(self):
        # representation d'un objet segment
        return "Segment : [(%g, %g), (%g, %g)]" % (self.orig.px, self.orig.py,
self.extrem.px, self.extrem.py)

#methode d'affichage
if __name__ == '__main__':
    s = Segment(1, 2, 3, 4)
    print (s)




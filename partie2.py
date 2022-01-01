class Etudiant:

    nom = ""
    prenom = ""
    age = 0
    cne = ""
    moyenne = 0

    def __init__(self, nom="", prenom="", age=0, cne="", moyenne=0):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
    def display(self):
        print("[",self.nom, "]","[", self.prenom, "]", "[",self.age, "]", "[", self.cne, "]", "[",self.moyenne , "]")


e1 = Etudiant("ahmed", "ahmad", 19, "p20202020", 11)
e2 = Etudiant("charaf", "saida", 10, "p20202020", 15)
e3 = Etudiant("sandwich", "kamal", 17, "p20202020", 5)
e4 = Etudiant("azzelzouli", "abdo", 0, "p20202020", 14)
e5 = Etudiant("chemmakh", "zoubida ", 17, "p20202020", 16)

ListEtudiants = []
ListEtudiants.append(e1)
ListEtudiants.append(e2)
ListEtudiants.append(e3)
ListEtudiants.append(e4)
ListEtudiants.append(e5)

#ordre selon l'age et la moyen :

def MySort1(etudiant):
    return -etudiant.moyenne - etudiant.age

# affichage par ordre selon l'age et la moyen :
ListEtudiants.sort(key=MySort1)
for i in ListEtudiants:
    i.display()


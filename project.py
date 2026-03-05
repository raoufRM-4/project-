class Parc:
    def __init__(self,id,adresse,capacite):
        self.id=id
        self.adresse=adresse
        self.capacite=capacite
        self.listvoiture=[]
    def entrer(self,voiture):
        if len(self.listvoiture)>=self.capacite:
            print("le parc est plein")
            return
        for i in self.listvoiture:
            if i.matricule==voiture.matricule:
                print("cette voiture est deja la ")
                return
        self.listvoiture.append(voiture)
        print("la voiture est bien ajouter")
    def sortir(self,voiture):
        for i in self.listvoiture:
            if i.matricule==voiture.matricule:
                self.listvoiture.remove(i)
                print("la voiture a ete bien suprimer")
                return
        print("la voiture est pas dans le parc")
    def les_places(self):
        a=self.capacite - len(self.listvoiture)
        print(f"il reste:{a} place ")
class Voiture:
    def __init__(self,matricule,marque,couleur):
        self.matricule=matricule
        self.marque=marque
        self.couleur=couleur
    def afficher(self):
        print(f"la matricule est:{self.matricule},la marque est:{self.marque}et la couleur est :{self.couleur}")

p1=Parc(300,"300 rue saint clair",3)
v1=Voiture("HB2 224","honda","noir")
v2=Voiture("CA 4556","ford","blanche")
v3=Voiture("BFD 85R","bmw","noir")
p1.entrer(v1)
p1.entrer(v1)
p1.entrer(v2)
p1.entrer(v3)
p1.sortir(v2)
p1.les_places()
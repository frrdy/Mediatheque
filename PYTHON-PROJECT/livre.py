from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class livre(objets):
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur,nombrepage,maisonedition,typel):
       super().__init__(idobjet,nom,auteur,datep,dateaj,typee,idutilisateur)
       self.nombrepage=nombrepage
       self.maisonedition=maisonedition
       self.typel=typel

    def ajout(self):
        lst2=[self.idobjet, self.nom, self.auteur, self.datep, self.dateaj, self.typee, self.idutilisateur]
        lst1=[self.idobjet, self.nombrepage,self.maisonedition,self.typel]
        cursor.execute(""" select idobjet from objets where idobjet= (?) """, (self.idobjet,))
        liste=list(cursor)
        print(liste)
        if liste==[]:
            cursor.execute(""" INSERT INTO livre (idobjet, nombrepage,maisonedition,typel) values (?,?,?,?) """, lst1)
            cursor.execute(""" INSERT INTO objets (idobjet, nom, auteur, datep, dateaj, typee,idutilisateur) values (?,?,?,?,?,?,?) """, lst2)
            conn.commit()
            print("Ajouté avec Succés")
        if liste!=[]:
            print("identifiant deja utilisé donc objet deja existant")

def supprimerL(identifiant):
            cursor.execute(""" select idobjet from objets where idobjet= (?) """, (identifiant,))
            liste = list(cursor)
            print(liste)
            if liste != []:
                cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (identifiant,))
                cursor.execute(""" DELETE FROM Livre WHERE idobjet= (?) """, (identifiant,))
                conn.commit()
                print("suppression effectuée avec succes")


def TLauteur(nomauteur):
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and objets.auteur=(?)""",
                   (nomauteur,))
    liste = list(cursor)
    print(liste)


def TLdatep(jour):
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and objets.datep=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)


def TLdateaj(jour):
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and objets.dateaj=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)


def TLmaisone(nom):
    cursor.execute(
        """ select * from objets, livre where objets.idobjet=livre.idobjet and livre.maisonedition=(?)""", (nom,))
    liste = list(cursor)
    print(liste)


def TLtypel(nom):
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and livre.typel=(?)""",
                   (nom,))
    liste = list(cursor)
    print(liste)
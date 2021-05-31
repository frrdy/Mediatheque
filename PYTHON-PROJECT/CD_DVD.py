from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class CD_DVD(objets):
    def __init__(self, idobjet, nom, auteur, datep, dateaj, typee,idutilisateur, duree,typeec):
            super().__init__(idobjet, nom, auteur, datep, dateaj,typee,idutilisateur)
            self.duree = duree
            self.typeec = typeec

    def ajout(self):
        lst2=[self.idobjet, self.nom, self.auteur, self.datep, self.dateaj, self.typee, self.idutilisateur]
        lst1=[self.idobjet, self.duree,self.typeec]
        cursor.execute(""" select idobjet from objets where idobjet= (?) """, (self.idobjet,))
        liste=list(cursor)
        print(liste)
        if liste==[]:
            cursor.execute(""" INSERT INTO CD_DVD (idobjet, duree,typec) values (?,?,?) """, lst1)
            cursor.execute(""" INSERT INTO objets (idobjet, nom, auteur, datep, dateaj, typee,idutilisateur) values (?,?,?,?,?,?,?) """, lst2)
            conn.commit()
            print("Ajouté avec Succés")
        if liste!=[]:
            print("identifiant deja utilisé donc objet deja existant")


def supprimerCD_DVD(identifiant):
         cursor.execute(""" select idobjet from objets where idobjet= (?) """, (identifiant,))
         liste = list(cursor)
         print(liste)
         if liste!=[]:
            cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (identifiant,))
            cursor.execute(""" DELETE FROM CD_DVD WHERE idobjet= (?) """, (identifiant,))
            conn.commit()
            print("suppression effectuée avec succes")

def TCDauteur(nomauteur):
        cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and objets.auteur=(?)""",
                       (nomauteur,))
        liste = list(cursor)
        print(liste)


def TCDdatep(jour):
    cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and objets.datep=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)


def TCDdateaj(jour):
    cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and objets.dateaj=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)


def TCDtypec(typecc):
    cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and CD_DVD.typec=(?)""",
                   (typecc,))
    liste = list(cursor)
    print(liste)

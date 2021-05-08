from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class magazine(objets):
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur,nombrepage,maisonedition,genre,frequence):
       super().__init__(idobjet,nom,auteur,datep,dateaj,typee,idutilisateur)
       self.nombrepage=nombrepage
       self.maisonedition=maisonedition
       self.genre=genre
       self.frequence=frequence


    def ajout(self):
        lst2=[self.idobjet, self.nom, self.auteur, self.datep, self.dateaj, self.typee, self.idutilisateur]
        lst1=[self.idobjet, self.nombrepage,self.maisonedition,self.genre,self.frequence]
        cursor.execute(""" select idobjet from objets where idobjet= (?) """, (self.idobjet,))
        liste=list(cursor)
        print(liste)
        if liste==[]:
            cursor.execute(""" INSERT INTO magazine (idobjet, nombrepage,maisonedition,genre,frequence) values (?,?,?,?,?) """, lst1)
            cursor.execute(""" INSERT INTO objets (idobjet, nom, auteur, datep, dateaj, typee,idutilisateur) values (?,?,?,?,?,?,?) """, lst2)
            conn.commit()
            print("Ajouté avec Succés")
        if liste!=[]:
            print("identifiant deja utilisé donc objet deja existant")

    def supprimer(self):
            cursor.execute(""" select idobjet from objets where idobjet= (?) """, (self.idobjet,))
            liste = list(cursor)
            print(liste)
            if liste != []:
                cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (self.idobjet,))
                cursor.execute(""" DELETE FROM magazine WHERE idobjet= (?) """, (self.idobjet,))
                conn.commit()
                print("suppression effectuée avec succes")

mag1=magazine(3332456734222,"A","A","03-04-2020","03-04-2021","magazine",1111,22,"lalala","politique","hebdomadaire")
mag1.ajout()
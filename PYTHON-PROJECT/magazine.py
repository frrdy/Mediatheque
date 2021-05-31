"""
@author: WANDJI K Frédérique
"""
from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class magazine(objets):
    """
    constructeur
    """
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur,nombrepage,maisonedition,genre,frequence):
       super().__init__(idobjet,nom,auteur,datep,dateaj,typee,idutilisateur)
       self.nombrepage=nombrepage
       self.maisonedition=maisonedition
       self.genre=genre
       self.frequence=frequence


    def ajout(self):
        """
        ajout d'un magazine
        """
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

def supprimerM(identifiant):
    """
    suppression d'un magazine à partir se son identifiant
    @param identifiant: identifiant du magazine à supprimer
    """
            cursor.execute(""" select idobjet from objets where idobjet= (?) """, (identifiant,))
            liste = list(cursor)
            print(liste)
            if liste != []:
                cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (identifiant,))
                cursor.execute(""" DELETE FROM magazine WHERE idobjet= (?) """, (ientifiant,))
                conn.commit()
                print("suppression effectuée avec succes")


def TMauteur(nomauteur):
    """
    Tri des magazines en fonction du nom de l'auteur
    @param nomauteur: nom de l'auteur
    @return: magazines dont le nom de l'auteur est passé en argument
    """
    cursor.execute(""" select * from objets, magazine where objets.idobjet=magazine.idobjet and objets.auteur=(?)""",
                   (nomauteur,))
    liste = list(cursor)
    print(liste)
    return liste


def TMdatep(jour):
    """
    Tri des magazines en fonction de la date de publication
    @param jour: date de publication
    @return: magazines dont la date de publication est passée en argument
    """
    cursor.execute(""" select * from objets, magazine where objets.idobjet=magazine.idobjet and objets.datep=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)
    return liste


def TMdateaj(jour):
    """
    Tri des magazines en fonction de la date d'ajout
    @param jour: date d'ajout
    @return: magazines dont la date d'ajout est passée en argument
    """
    cursor.execute(""" select * from objets, magazine where objets.idobjet=magazine.idobjet and objets.dateaj=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)
    return liste


def TMmaisone(nom):
    """
    Tri des magazines en fonction du nom de la maison d'édition
    @param nom: om de la maison d'édition
    @return: magazines dont le nom de la maison d'édition est passé en argument
    """
    cursor.execute(
        """ select * from objets, magazine where objets.idobjet=magazine.idobjet and magazine.maisonedition=(?)""", (nom,))
    liste = list(cursor)
    print(liste)
    return liste


def TMfrequence(freq):
    """
    Tri des magazines en fonction de la fréquence
    @param freq: fréquence
    @return: magazines dont la fréquence est passée en argument
    """
    cursor.execute(""" select * from objets, magazine where objets.idobjet=magazine.idobjet and magazine.frequence=(?)""",
                   (freq,))
    liste = list(cursor)
    print(liste)
    return liste

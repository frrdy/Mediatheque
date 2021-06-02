"""
@author: WANDJI K Frédérique
"""
from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class livre(objets):
    """
    constructeur
    """
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur,nombrepage,maisonedition,typel):
       super().__init__(idobjet,nom,auteur,datep,dateaj,typee,idutilisateur)
       self.nombrepage=nombrepage
       self.maisonedition=maisonedition
       self.typel=typel

    def ajout(self):
        """
        Ajout d'un livre
        """
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
    """
    suppression d'un livre à partir de son identifiant
    @param identifiant: identifiant du livre à supprimer
    """
    cursor.execute(""" select idobjet from objets where idobjet= (?) """, (identifiant,))
    liste = list(cursor)
    print(liste)
    if liste != []:
      cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (identifiant,))
      cursor.execute(""" DELETE FROM Livre WHERE idobjet= (?) """, (identifiant,))
      conn.commit()
      print("suppression effectuée avec succes")


def TLauteur(nomauteur):
    """
    Fonction pour le tri des livres en fonction du nom de l'auteur
    @param nomauteur: nom de l'auteur
    @return: livres dont le nom de l'auteur est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and objets.auteur=(?)""",
                   (nomauteur,))
    liste = list(cursor)
    print(liste)
    return liste

def TLdatep(jour):
    """
    Fonction pour le tri des livres en fonction de la date de publication
    @param jour: date de publication
    @return: livres dont la date de publication est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and objets.datep=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)
    return liste


def TLdateaj(jour):
    """
    Fonction pour le tri des livres en fonction de la date d'ajout
    @param jour: date d'ajout
    @return: livres dont la date d'ajout est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and objets.dateaj=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)
    return liste


def TLmaisone(nom):
    """
    Fonction pour le tri des livres en fonction du nom de la maison d'édition
    @param nom: nom de la maison d'édition
    @return: livres dont le nom de la maison d'édition est donné en argument de la fonction
    """
    cursor.execute(
        """ select * from objets, livre where objets.idobjet=livre.idobjet and livre.maisonedition=(?)""", (nom,))
    liste = list(cursor)
    print(liste)
    return liste


def TLtypel(nom):
    """
   Fonction pour le tri des livres en fonction du type
    @param nom: type
    @return: livres dont le type est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, livre where objets.idobjet=livre.idobjet and livre.typel=(?)""",
                   (nom,))
    liste = list(cursor)
    print(liste)
    return liste
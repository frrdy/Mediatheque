"""
@author: WANDJI K Frédérique
"""
from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class journal(objets):
    """
    constructeur
    """
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur,nombrepage,maisonedition,typej):
       super().__init__(idobjet,nom,auteur,datep,dateaj,typee,idutilisateur)
       self.nombrepage=nombrepage
       self.maisonedition=maisonedition
       self.typej=typej

    def ajout(self):
        """

        ajout d'un journal
        """
        lst2=[self.idobjet, self.nom, self.auteur, self.datep, self.dateaj, self.typee, self.idutilisateur]
        lst1=[self.idobjet, self.nombrepage,self.maisonedition,self.typej]
        cursor.execute(""" select idobjet from objets where idobjet= (?) """, (self.idobjet,))
        liste=list(cursor)
        print(liste)
        if liste==[]:
            cursor.execute(""" INSERT INTO journal (idobjet, nombrepage,maisonedition,typej) values (?,?,?,?) """, lst1)
            cursor.execute(""" INSERT INTO objets (idobjet, nom, auteur, datep, dateaj, typee,idutilisateur) values (?,?,?,?,?,?,?) """, lst2)
            conn.commit()
            print("Ajouté avec Succés")
        if liste!=[]:
            print("identifiant deja utilisé donc objet deja existant")

def supprimerJ(identifiant):
    """
    suppression d'un journal en fonction de son identifiant
    @param identifiant: identifiant du journal à supprimer
    """
    cursor.execute(""" select idobjet from objets where idobjet= (?) """, (identifiant,))
    liste = list(cursor)
    print(liste)
    if liste != []:
        cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (identifiant,))
        cursor.execute(""" DELETE FROM journal WHERE idobjet= (?) """, (identifiant,))
        conn.commit()
        print("suppression effectuée avec succes")


def TJauteur(nomauteur):
    """
    fonction pour le tri des  journaux en fonction du nom de l'auteur
    @param nomauteur: nom de l'auteur des journaux
    @return: les journaux dont le nom de l'auteur est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, journal where objets.idobjet=journal.idobjet and objets.auteur=(?)""",(nomauteur,))
    liste = list(cursor)
    print(liste)

def TJdatep(jour):
    """
     fonction pour le tri des  journaux en fonction de la date de publication
    @param jour: date de publication des journaux
    @return: les journaux dont la date de publication est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, journal where objets.idobjet=journal.idobjet and objets.datep=(?)""",(jour,))
    liste = list(cursor)
    print(liste)

def TJdateaj(jour):
    """
    fonction pour le tri des  journaux en fonction de la date d'ajout
    @param jour: date d'ajout des journaux
    @return: les journaux dont la date d'ajout est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, journal where objets.idobjet=journal.idobjet and objets.dateaj=(?)""",(jour,))
    liste = list(cursor)
    print(liste)

def TJmaisone(nom):
    """
    fonction pour le tri des  journaux en fonction du nom de la maison d'édition
    @param nom: nom de la maison d'édition des journaux
    @return: les journaux dont le nom de la maison d'édition est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, journal where objets.idobjet=journal.idobjet and journal.maisonedition=(?)""",(nom,))
    liste = list(cursor)
    print(liste)

def TJtypej(nom):
    """
    fonction pour le tri des  journaux en fonction de leur type(documentaire, ...)
    @param nom:  type des journaux
    @return: les journaux dont le type est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, journal where objets.idobjet=journal.idobjet and journal.typej=(?)""",(nom,))
    liste = list(cursor)
    print(liste)
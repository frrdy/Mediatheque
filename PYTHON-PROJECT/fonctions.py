"""
@author: WANDJI K Frédérique
"""
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()






class objets(object):
    """
    Constructeur de la classe mere
    """
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur):
        self.idobjet=idobjet
        self.nom=nom
        self.auteur=auteur
        self.datep=datep
        self.dateaj=dateaj
        self.typee=typee
        self.idutilisateur=idutilisateur





def afficherCD_DVD():
    """
    fonction pour l'affichage de tous les CD/DVD
    @return: les CD/DVD
    """"
        cursor.execute("""SELECT * FROM objets, CD_DVD where objets.idobjet=CD_DVD.idobjet""")
        liste = list(cursor)
        return liste



def afficherlivre():
    """
   fonction pour l'affichage de tous les livres
    @return: les livres
    """
    cursor.execute("""SELECT * FROM objets,livre where objets.idobjet=livre.idobjet""")
    liste = list(cursor)
    return liste


def afficherjournal():
    """
    fonction pour l'affichage de tous les journaux
    @return: les journaux
    """
    cursor.execute("""SELECT * FROM objets,journal where objets.idobjet=journal.idobjet""")
    liste = list(cursor)
    return liste




def affichermagazine():
    """
   fonction pour l'affichage de tous les magazines
    @return: les magazines
    """
    cursor.execute("""SELECT * FROM objets,magazine where objets.idobjet=magazine.idobjet""")
    liste = list(cursor)
    return liste


def afficher():
    """

   affichage de tous les élements
    """
    afficherCD_DVD()
    afficherlivre()
    afficherjournal()
    affichermagazine()

def afficherIDC(identifiant):
    """
    fonction pour l'affichage d'un CD/DVD en fonction de son identifiant
    @param identifiant: identifiant du CD/DVD recherché
    @return: CD/DVD recherché
    """
    cursor.execute(""" SELECT * FROM objets, CD_DVD where objets.idobjet=(?) AND objets.idobjet=CD_DVD.idobjet  """,(identifiant,))
    liste=list(cursor)
    return liste

def afficherIDJ(identifiant):
    """
   fonction pour l'affichage d'un journal en fonction de son identifiant
    @param identifiant: identifiant du journal recherché
    @return: journal recherché
    """
    cursor.execute(""" SELECT * FROM objets, journal where objets.idobjet=(?) AND objets.idobjet=journal.idobjet  """,(identifiant,))
    liste=list(cursor)
    return liste

def afficherIDL(identifiant):
    """
    fonction pour l'affichage d'un livre en fonction de son identifiant
    @param identifiant: identifiant du livre recherché
    @return: livre recherché
    """
    cursor.execute(""" SELECT * FROM objets, livre where objets.idobjet=(?) AND objets.idobjet=livre.idobjet  """,(identifiant,))
    liste=list(cursor)
    return liste

def afficherIDM(identifiant):
    """
   fonction pour l'affichage d'un magazine en fonction de son identifiant
    @param identifiant: identifiant du magazine recherché
    @return: magazine recherché
    """
    cursor.execute(""" SELECT * FROM objets, magazine where objets.idobjet=(?) AND objets.idobjet=magazine.idobjet  """,(identifiant,))
    liste=list(cursor)
    return liste


#obj1=CD_DVD(33322995654,"k","k","03-04-2020","03-04-2021","CD-DVD","1111","2:00:00","documentaire")
#liv1=livre(33322,"A","A","03-04-2020","03-04-2021","livre",1111,22,"lalala","documentaire")
#liv1.supprimer()
#obj1.supprimer()
#jou1=journal(33324322,"A","A","03-04-2020","03-04-2021","journal",1111,22,"lalala","politique")
#jou1.supprimer()
#mag1=magazine(3332456734222,"A","A","03-04-2020","03-04-2021","magazine",1111,22,"lalala","politique","hebdomadaire")
#mag1.supprimer()
#afficher()
#afficherCD_DVD()

# affichermagazine()
# afficherjournal()
# afficherlivre()

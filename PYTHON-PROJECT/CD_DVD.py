from fonctions import objets
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class CD_DVD(objets):
    """
    constructeur
    """
    def __init__(self, idobjet, nom, auteur, datep, dateaj, typee,idutilisateur, duree,typeec):
            super().__init__(idobjet, nom, auteur, datep, dateaj,typee,idutilisateur)
            self.duree = duree
            self.typeec = typeec

    def ajout(self):
        """
        @author: WANDJI K. Frédérique
        fonction permettant l'ajout d'un objet de type CD/DVD
        """
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
    """
    @author: WANDJI K. Frédérique
    Fonction permettant la suppression d'un objet de type CD/DVD à partir de son identifiant
    @param identifiant: parametre représentant l'identifiant de l'objet à supprimer
    """
    cursor.execute(""" select idobjet from objets where idobjet= (?) """, (identifiant,))
    liste = list(cursor)
    print(liste)
    if liste!=[]:
            cursor.execute(""" DELETE FROM objets WHERE idobjet= (?) """, (identifiant,))
            cursor.execute(""" DELETE FROM CD_DVD WHERE idobjet= (?) """, (identifiant,))
            conn.commit()
            print("suppression effectuée avec succes")

def TCDauteur(nomauteur):
        """
        @author: WANDJI K. Frédérique
        fonction permettant le tri des CD/DVD en fonction du nom de l'auteur
        @param nomauteur: parametre répresentant le nom de l'auteur
        @return: CD/DVD dont le nom de l'auteur est donné en argument de la fonction
        """
        cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and objets.auteur=(?)""",
                       (nomauteur,))
        liste = list(cursor)
        print(liste)
        return liste


def TCDdatep(jour):
    """
    @author: WANDJI K. Frédérique
    fonction permettant le tri des CD/DVD en fonction de la date de publication
    @param jour: parametre répresentant la date de publication
    @return: CD/DVD dont la date de publication est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and objets.datep=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)
    return liste


def TCDdateaj(jour):
    """
    @author: WANDJI K. Frédérique
        fonction permettant le tri des CD/DVD en fonction de la date d'ajout du CD/DVD '
        @param jour: parametre répresentant la date d'ajout
        @return: CD/DVD dont la date d'ajout est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and objets.dateaj=(?)""",
                   (jour,))
    liste = list(cursor)
    print(liste)
    return liste


def TCDtypec(typecc):
    """
    @author: WANDJI K. Frédérique
        fonction permettant le tri des CD/DVD en fonction de leur type(documentaire,...) '
        @param jour: parametre répresentant le type du CD/DVD
        @return: CD/DVD dont le type est donné en argument de la fonction
    """
    cursor.execute(""" select * from objets, CD_DVD where objets.idobjet=CD_DVD.idobjet and CD_DVD.typec=(?)""",
                   (typecc,))
    liste = list(cursor)
    print(liste)
    return liste

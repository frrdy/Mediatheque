import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()






class objets(object):
    def __init__(self,idobjet,nom,auteur,datep,dateaj,typee,idutilisateur):
        self.idobjet=idobjet
        self.nom=nom
        self.auteur=auteur
        self.datep=datep
        self.dateaj=dateaj
        self.typee=typee
        self.idutilisateur=idutilisateur





def afficherCD_DVD():
        cursor.execute("""SELECT * FROM objets, CD_DVD where objets.idobjet=CD_DVD.idobjet""")
        liste = list(cursor)
        print(liste)



def afficherlivre():
    cursor.execute("""SELECT * FROM objets,livre where objets.idobjet=livre.idobjet""")
    liste = list(cursor)
    print(liste)


def afficherjournal():
    cursor.execute("""SELECT * FROM objets,journal where objets.idobjet=journal.idobjet""")
    liste = list(cursor)
    print(liste)




def affichermagazine():
    cursor.execute("""SELECT * FROM objets,magazine where objets.idobjet=magazine.idobjet""")
    liste = list(cursor)
    print(liste)


def afficher():
    afficherCD_DVD()
    afficherlivre()
    afficherjournal()
    affichermagazine()


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

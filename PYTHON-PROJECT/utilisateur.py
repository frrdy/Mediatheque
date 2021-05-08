import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class utilisateur(object):
    def __init__(self,id,mdp):
        self.id=id
        self.mdp=mdp

    def ajout(self):
        lst=[self.id,self.mdp]
        cursor.execute("""SELECT identifiant FROM utilisateur where identifiant=(?)""",(self.id,))
        liste = list(cursor)
        print(liste)
        if liste==[]:
         cursor.execute(""" INSERT INTO utilisateur (identifiant,mot_passe) values (?,?) """, lst)
         conn.commit()
        else:
          print("identifiant deja utilisé")

    def connexion(self):
        lst = [self.id, self.mdp]
        cursor.execute("""SELECT identifiant FROM utilisateur where identifiant=(?) and mot_passe=(?)""", (lst[0],lst[1]))
        liste = list(cursor)
        print(liste)
        if liste == []:
            print("connexion impossible. Identifiant ou mot de passe incorrect")
        else:
            print("établit avec succes ")


    def supprimer(self):
        lst = [self.id, self.mdp]
        cursor.execute("""SELECT identifiant FROM utilisateur where identifiant=(?)""", (self.id,))
        liste = list(cursor)
        print(liste)
        if liste != []:
            cursor.execute(""" DELETE FROM utilisateur WHERE identifiant=(?)""", (lst[0],))
            conn.commit()
            print("suppression effectué avec succes ")
        else:
            print("--")
user=utilisateur("1111","1111")
user.supprimer()
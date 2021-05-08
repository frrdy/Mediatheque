import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateur(
     identifiant TEXT PRIMARY KEY UNIQUE,
     mot_passe TEXT
) 
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS objets(
     idobjet TEXT PRIMARY KEY UNIQUE,
     nom TEXT,
     auteur TEXT,
     datep date,
     dateaj date default current_date ,
     typee TEXT,
     idutilisateur TEXT,
     CONSTRAINT fk_idutilisateur FOREIGN KEY (idutilisateur) REFERENCES utilisateur(identifiant)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CD_DVD(
     idobjet TEXT PRIMARY KEY UNIQUE,
     duree time,
     typec TEXT,
     CONSTRAINT fk_idobjet FOREIGN KEY (idobjet) REFERENCES objets(idobjet)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS journal(
     idobjet TEXT PRIMARY KEY UNIQUE,
     nombrepage INTEGER,
     maisonedition TEXT,
     typej TEXT,
     CONSTRAINT fk_idobjet FOREIGN KEY (idobjet) REFERENCES objets(idobjet)    
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livre(
     idobjet TEXT PRIMARY KEY UNIQUE,
     nombrepage INTEGER,
     maisonedition TEXT,
     typel TEXT,
     CONSTRAINT fk_idobjet FOREIGN KEY (idobjet) REFERENCES objets(idobjet)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS magazine(
     idobjet TEXT PRIMARY KEY UNIQUE,
     nombrepage INTEGER,
     maisonedition TEXT,
     genre TEXT,
     frequence TEXT,
     CONSTRAINT fk_idobjet FOREIGN KEY (idobjet) REFERENCES objets(idobjet)
)    
""")
conn.commit()
conn.close()
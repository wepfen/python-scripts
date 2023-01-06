
import os, re, shutil
""" ce programme va venir classer les fichiers par année dans différents sous-dossiers des années correspondantes"""


#regex pour trouver l'année dans le nom du fichier : (20)[0-9]{2}

dirpath = str(input('Entrer le répertoire du dossier à organiser : '))  # lerepertoire des fichiers


listeFichiers = []

for (repertoire, sousRepertoires, fichiers) in os.walk(dirpath):  #récupère les fichiers
    listeFichiers.extend(fichiers)

def main():
    for fichier in listeFichiers:
        regex(fichier)

def regex(fichier): #tente d'extraire l'année du fichier
    regexp = "(20)[0-9]{2}" #expression servant à trouver l'année du fichier dans son nom
    res = re.search(regexp, fichier).group(0) #il s'agit du résultat après la recherche par regex

    try:
        int(res) #classe le fichier si c'est un succès
        classer(fichier, res)
    except:
        pass

    return None

def classer(fichier, res): 
    filepath = f"{dirpath}\{fichier}" #chemin du fichier 
    newdir = f"{dirpath}\{res}" #dossier par année 
    newfilepath = f"{newdir}\{fichier}" #nouvelle destination du fichier

    if os.path.isdir(newdir) == True:
        shutil.move(f"{filepath}" , f"{newfilepath}")
    if os.path.isdir(newdir) == False:
        os.mkdir(f"{newdir}")
        shutil.move(f"{filepath}" , f"{newfilepath}")

    return None

main()
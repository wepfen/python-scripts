import requests

# requete l'etudiant en get: https://www.letudiant.fr/resultat/recherche.html?researcher%5Bnom%5D={nom}&researcher%5Bexamen%5D={diplome}&researcher%5Bacademie%5D={academie}
# requete l'internaute: https://resultat-bts.linternaute.com/academie-versailles#search=''ezez
# requete parisien: https://www.leparisien.fr/etudiant/examens/resultats/bts/paris-creteil-versailles/candidat/nom/prenom/

nom = str(input("nom ? "))
prenom = str(input("prenom ? "))
academie = str(input("academie ? ")) 
diplome = "bts" #remplacer par input

def main():
    
    print(letudiant())
    #print(internaute())
    print(leparisien())

    
def letudiant(): # recherche vers le site letudiant
    
    r_letudiant = requests.get(f'https://www.letudiant.fr/resultat/recherche.html?researcher%5Bnom%5D={nom}&researcher%5Bexamen%5D={diplome}&researcher%5Bacademie%5D={academie}')
    
    #print(r_letudiant.status_code) #verifie si la requete fonctionne
    r_letudiant_response = r_letudiant.text
    if "aucun résultat" in r_letudiant.text:
        return "[-] L'étudiant: Aucun résultat"
    else:
        return "[+] L'étudiant: Résultats disponibles"

def internaute(): #marche pas
    
    r_internaute = requests.get(f'https://resultat-bts.linternaute.com/academie-{academie.lower()}#search={nom.lower()}')
    
    #print(r_internaute.status_code)
    
    r_internaute_response = r_internaute.text
    if "aucun résultat" in r_internaute.text:
        return "[-] L'internaute: Aucun résultat"
    else:
        return "[+] L'internaute: Résultats disponibles (pour une ou plusieurs personnes de ce nom et de cette académie)"
    
def leparisien(): 
    
    if academie == "versailles":
        temp_academie = "paris-creteil-versailles"
    
    r_parisien = requests.get(f'https://www.leparisien.fr/etudiant/examens/resultats/bts/{temp_academie}/candidat/{nom}/{prenom}/')
    
    if "0 résultat" in r_parisien.text:
        return "[-] Le parisien: Aucun résultat"
    else:
        return "[+] Le parisien: Résultats disponibles"
  

if __name__ == "__main__":
    main()
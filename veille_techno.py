#this script is a choice script that open a news webpage for the subject selected by the user. I created this to automatize articles research for a school project

import webbrowser, feedparser, os


sites = [
        ["zataz", "https://www.zataz.com/", ["cybersécurité"]],
        ['lemondeinformatique', 'https://www.lemondeinformatique.fr/',['cybersécurité','informatique en général']],
        ["google alert", "https://www.google.com/",['métaverse']]
        ]

feeds = [ #les liens sont dans le meme ordre que dans la liste sites et donc que les choix effectués
    ['https://www.zataz.com/feed/'],
    ['https://www.lemondeinformatique.fr/flux-rss/thematique/securite/rss.xml','https://www.lemondeinformatique.fr/flux-rss/thematique/toutes-les-actualites/rss.xml'],
    ['https://www.google.com/alerts/feeds/16885718539224405068/7966756002791873134']
]
feed_path = [] #mene au chemin vers le bon feed, se remplit auto durant le script

liens_articles = [] #se remplira automatiquement lors de l'affichage des articles

def main():
    choix_site()

def choix_site():
    global sites

    os.system('cls') #cls, la commande batch
    i = 0
    while i < len(sites): #affiche les sites et leur index pour pouvoir en choisir un
        print(f"[{i}] {sites[i][0]}")
        i += 1

    choice = input_choix(len(sites),'du site') #choix du site
    feed_path.append(choice) #sauvegarde du choix 

    
    os.system('cls') 
    i = 0
    while i < len(sites[choice][2]): #affiche les sujets du site choisi et leur index pour pouvoir en choisir un ensuite
        print(f"[{i}] {sites[choice][2][i]}")
        i += 1

    nb_choix = len(sites[choice][2])
    choice = input_choix(nb_choix, "du sujet") #choix du sujet
    feed_path.append(choice)
    feed = feeds[feed_path[0]][feed_path[1]]
    
    article=input_choix(afficher_article(feed),"de l'article")
    choix_article(article)
    
    #aller cherche le feed correspondant au sujet et au site et le mettre en variable pour la fonction

     
def input_choix(nb_choix, nom_choix): #retourne l'index choisi
    nb_choix-=1

    while True: 
        
        try:
            choice = int(input(f"Entrez l'index  {nom_choix} : ")) # choix du site
            if 0 <= choice <= nb_choix:
                return choice 

        except:
            print(f' \nEntrez une saisie valide (entre 0 et {nb_choix}) ') # si la saisie est incorrecte ou la valeur pas dans la liste, la boucle recommence

def afficher_article(feed): #affiche les articles trouvs
    i = 0
    while True: 
        try:
            news_feed = feedparser.parse(feed)
            print(f'[{i}]{news_feed.entries[i].title}')
            liens_articles.append(news_feed.entries[i].link)
            i += 1
        except:
            return i

def choix_article(id): #feed = le feed de la page a check et id le l'index de l'article qu'on a rentré juste avant

    link = liens_articles[id]
    print(link)
    webbrowser.open(link)

main()

#lorsque le site est choisi, definir la variable news_feed avec le choix
#site de doc https://blog.jbriault.fr/rss-python/

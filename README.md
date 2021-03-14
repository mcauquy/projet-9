# projet-9
Vous trouverez ici la fonction Azure: Contentbase
Cette fonction a pour objectif de trouver 5 recommandations de lecture pour un utilisateur.

Cette fonction permet de recevoir le UserID de l'app Bookshelf permettant de préparer la recommandation de 5 articles pour ce User et de la renvoyer vers l'app Bookshelf.

Le fichier load_data.py permet de charger les informations permettant de calculer les recommandations.
Les informations pertinants sont stockées dans le répertoire globocom.
Vous y trouverez les informations suivantes:
- clicks des différents user
- les informations relatives aux articles
- une matrice représentant les différents articles au format numérique (embedding)

Le fichier cont_based.py permet de calculer les recommandations.
Cette fonction est basée sur la méthode 'Content based' c'est à dire que la distance entre l'article de référence et les autres articles est calculée (en utilisant la matrice embedding).
Les articles ayant la distance minimale sont les plus similaires et seront donc proposés comme recommandation.

Pour faire fonctionner l'app Bookshelf et cette fonction Azure, il faut modifier le fichier config.json pour y insérer l'URL de la fonction Azure:
![image](https://user-images.githubusercontent.com/78112098/111081097-dfbb7d00-8501-11eb-9810-63b23d2c5116.png)

{
  "API_URL": "http://localhost:7071/api/Contentbase"
}


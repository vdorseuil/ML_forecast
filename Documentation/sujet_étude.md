Pour résumer le contenu :

Dans plusieurs pays européens il y a des enchères de services systèmes, notamment une qui s'appelle l'automatic Frequency Restoration Reserve (aFRR), qui vise à permettre au système électrique de solliciter des productions d'électricité en plus ou en moins en temps réel. L'enchère se tient tous les jours vers 8h pour les livraisons d'électricité du lendemain, et il y a 12 produits : pour l'accroissement de production entre 0h et 4h  (POS_00_04), la baisse de production entre 0 h et 4h (NEG_00_04), l'accroissement entre 4h et 8h (POS_04_08), ... vous voyez l'idée. On peut considérer que ce sont des produits indépendants les uns des autres.
Il y a chaque jour une demande pour chacun des 12 produits, publiée à l'avance par l'organisateur. Puis les participants au marché soumettent des courbes d'offre (volume / prix) qui sont empilées par ordre de prix croissant jusqu'à ce que la somme des volumes atteigne la demande. Le prix de la dernière offre qui permet de rencontrer la demande forme le prix d'équilibre,  c'est le prix de l'aFRR pour ce créneau horaire.

Je pense que vous pouvez étudier la série temporelle des prix d'équilibre : soit pour un produit donné (par exemple la série temporelle des POS_00_04) soit pour le vecteur 12-dimensionnel des prix d'équilibre de chaque journée.

Dans l'archive j'ai mis ces informations mais aussi l'intégralité des offres acceptées chaque jour (ce qui veut dire que les offres soumises et non retenues ne sont pas publiées) si vous voulez les investiguer. Mais dans ce cas dites-nous, il faudra que nous vous détaillions un peu plus certaines colonnes des fichiers. Voici le contenu de l'archive, en anglais :

LIST_OF_TENDERS...xlsx: for every day between January 1st, 2024 and August 31st, 2024, 12 lines featuring the 12 auction products. On each line, you will find the date, the name of the product (e.g. POS_00_04), the demand in Germany and Austria (*_BLOCK_DEMAND). The demand in Austria is constant, except that it increased on August 13th. In Germany it is varying, you may either take it as is, or assume it to be constant for the numerical experiments.
-    RESULT_OVERVIEW...xlsx: some statistics on the same period. Among others there is the equilibrium price in Germany in column J and in Austria in column N. So this file might be the only one you actually need.
RESULT_LIST...zip: 8 zip files, one per month from January, 2024 to August, 2024, with the list of all accepted offers for every day and each of the 12 auctions. One may have an idea about the number of losing bids by looking at the last column of the previous file and comparing it to the sum of the accepted bids in Germany for every day and auction. In these files, there is a column with "AT" or "DE" to see where the bid was made. For some reason, bids (of which size should be at least 1 MW, and be an integer) mostly have a size of 5MW, although they are not limited! I asked one of my colleagues, he observed that too but has no explanation.
Dites-nous ce que vous pensez pour le créneau d'entretien, et si la description des données est suffisante. Sinon je compléterai !

Bien cordialement,

--
Pierre Gruet
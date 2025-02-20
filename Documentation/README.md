# Machine learning : forecasting. Project by Valentin Dorseuil, Théo Gaboriaud. Course by Yannig Goude.


## Sujet :
Si vous le souhaitez, nous pouvons vous proposer un projet visant à effectuer des prévisions probabilistes de prix sur certaines enchères sur le marché d'électricité, enchères qui se tiennent tous les jours selon un certain calendrier : il y en a (mettons) trois, qui ont certains liens. La prévision peut se nourrir de l'historique bien évidemment, mais aussi des autres enchères de ce jour-là. Les données sont publiques et prises sur https://www.regelleistung.net/apps/datacenter/tenders/?productTypes=PRL%2CSRL%2CMRL%2CABLA&markets=BALANCING_CAPACITY%2CBALANCING_ENERGY&date=2024-10-29
(nous pourrons les extraire pour vous), nous vous laissons nous reconfirmer votre intérêt et nous pourrons alors prévoir un petit point d'échange avec vous deux pour préciser les choses.



# Explication sur les différents marchés de l'électricité :
## Les 3 marchés
1. Marché de l’Énergie (ou Marché Spot)
Ce marché couvre l’achat et la vente d’électricité pour répondre à la demande prévue. Il est divisé en sous-marchés :
- Marché Day-Ahead (DA) : C’est l’enchère principale où l’électricité est achetée et vendue la veille pour chaque heure de la journée suivante. Les prix sont déterminés par l'offre et la demande sur chaque créneau horaire.
- Marché Intra-Day (ID) : Sur ce marché, les transactions se font le jour même pour ajuster l’offre et la demande en fonction des prévisions actualisées, par exemple pour des variations météorologiques affectant la production éolienne ou solaire.
2. Marché des Réserves (ou Marché d’Équilibrage)
Ce marché spécifique vise à garantir des réserves de capacité pour l’équilibrage en cas d’imprévu. Il comprend les appels d’offres pour les services de réserves de fréquence (FCR, aFRR, mFRR), qui sont réservés en avance et activés seulement en cas de besoin pour maintenir la stabilité du réseau.
Ce segment inclut des enchères de capacité où les fournisseurs sont rémunérés pour mettre leur capacité à disposition, ainsi que des paiements pour l’énergie réellement activée lors d’un déséquilibre.
3. Marché d’Équilibrage en Temps Réel
En cas de déséquilibre non prévu entre offre et demande, les gestionnaires de réseau peuvent également activer des ajustements en temps réel. Ce marché permet d’équilibrer le réseau au prix de l’énergie d’équilibrage (généralement plus élevé en raison de l’urgence de la demande).


## En cas de déséquilibre: 
- Étape 1 : En cas de déséquilibre, le gestionnaire active d’abord les réserves de capacité déjà contractées (FCR, aFRR, mFRR).
- Étape 2 : Si les réserves de capacité ne suffisent pas, le gestionnaire de réseau passe au marché d’équilibrage en temps réel pour acheter l’énergie supplémentaire nécessaire.

## Détail du marché de réserve


### 1. **FCR (Frequency Containment Reserve)**
   - **Purpose:** FCR is used for primary frequency control, which is the first level of defense against frequency deviations on the power grid. When the grid frequency deviates from its nominal value (e.g., 50 Hz in Europe), FCR responds almost instantly to bring it back within a stable range.
   - **Activation Time:** Typically, within seconds (automated).
   - **Application:** FCR is shared across the European grid to ensure stability across interconnected countries.

### 2. **aFRR (Automatic Frequency Restoration Reserve)**
   - **Purpose:** aFRR is the secondary reserve that automatically adjusts power output to restore the grid frequency to its nominal value. It supports FCR but has a slightly longer activation time.
   - **Activation Time:** Within 30 seconds to a few minutes, responding automatically to signals from the transmission system operator (TSO).
   - **Application:** Used to correct smaller imbalances over a short period and is managed nationally, though it can be coordinated across borders.

### 3. **mFRR (Manual Frequency Restoration Reserve)**
   - **Purpose:** This is a tertiary reserve that is manually activated to restore grid balance after frequency issues have been addressed by FCR and aFRR. It is often used to manage longer-lasting or larger imbalances and to free up aFRR resources.
   - **Activation Time:** Ranges from a few minutes to around 15 minutes.
   - **Application:** Usually activated by request from the TSO, often involving larger power plants or load-shedding measures.

### 4. **ABLA (Automatic Balancing)**
   - **Purpose:** While the term "ABLA" might be shorthand or a specific acronym in certain regions, generally, automatic balancing in the European context refers to automated systems and algorithms that handle balancing services like aFRR, integrating renewable sources, and enhancing grid stability.
   - **Application:** Integrates with systems such as aFRR to provide ongoing balance without the need for manual intervention, leveraging technology for efficient grid operations.


## Tableau récapitulatif: 
Voici un tableau récapitulatif intégrant les informations clés des précédents messages :

| **Aspect**                     | **Marché des Enchères de Réserve (ou Marché de Capacité d’Équilibrage)** | **Marché d’Équilibrage en Temps Réel** | **Marché de l’Énergie (Spot)**                    |
|--------------------------------|---------------------------------------------------------------------------|----------------------------------------|----------------------------------------------------|
| **Objectif**                   | Assurer la **disponibilité de réserves** pour équilibrer le réseau en cas de besoin | Corriger les **déséquilibres imprévus en temps réel** | Couvrir la **demande prévue** d'électricité       |
| **Quand sont faites les enchères ?** | À l’avance (quotidien, hebdomadaire, mensuel) pour garantir la capacité de réserve | Activation en temps réel selon les déséquilibres | - **Day-Ahead** : La veille pour chaque heure du jour suivant<br> - **Intra-Day** : Ajustement le jour même |
| **Types de Réserves**          | - FCR : Réserve primaire de fréquence (réponse quasi-instantanée)<br>- aFRR : Réserve secondaire (réponse rapide)<br>- mFRR : Réserve tertiaire (réponse en quelques minutes)<br>- RR : Réserve de remplacement | Pas de type de réserve spécifique<br>Déclenché en cas d’urgence supplémentaire | Non applicable aux réserves, destiné à la couverture de la demande |
| **Rémunération**               | - **Disponibilité** : Les fournisseurs sont payés pour la capacité mise à disposition (même si elle n’est pas activée) et en plus si activéee | - **Énergie activée** : Les fournisseurs sont payés pour l’énergie injectée ou retirée du réseau en temps réel | - **Énergie fournie** : Payée en fonction de l'offre et la demande sur les sous-marchés DA et ID |
| **Priorité d’Activation**      | Première étape d’activation en cas de déséquilibre | Deuxième étape si les réserves ne suffisent pas | Non concerné par l'activation pour l'équilibrage |
| **Exemples de Fournisseurs**   | - Centrales à réaction rapide (gaz, hydroélectrique)<br>- Batteries de stockage<br>- Sites industriels (effacement de charge)<br>- Agrégateurs de petits consommateurs | - Centrales disponibles à l’instant<br>- Autres sources prêtes en temps réel (production ou consommation flexible) | - Producteurs traditionnels (éolien, solaire, nucléaire, etc.) |
| **Prix de l’Énergie**          | Pas applicable pour l’activation d’énergie ; basé sur la disponibilité réservée | Généralement plus élevé car lié à une activation urgente | Dépend de l’offre et la demande pour chaque créneau horaire (prix spot) |

### Processus d’Équilibrage
1. **Activation des Réserves de Capacité** : En cas de déséquilibre, les réserves de capacité (FCR, aFRR, mFRR) achetées à l’avance sont activées en premier lieu.
2. **Passage au Marché d’Équilibrage en Temps Réel** : Si les réserves de capacité ne suffisent pas, le gestionnaire de réseau recourt à l’achat d’énergie en temps réel pour stabiliser le réseau.
3. **Marché de l’Énergie (Spot)** : En dehors de l’équilibrage, ce marché répond aux besoins prévus de la demande.
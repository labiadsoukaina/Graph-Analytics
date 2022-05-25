### 2.1 - Le voyageur du Monde

c'est fait.

### 2.2 - La fainéantise du voyageur

Choix d'algorithme: Minimum Weight Spanning Tree.

Il s'agit ici d'un problème de marche aléatoire qu'on peut résoudre en utilisant l'algorithme "Minimum Weight Spanning Tree", qui cherche à partir d'un noeud donné (aéroport de départ) tous les noeuds atteignables (aéroports de destination) ainsi que l'ensemble des relations qui relient les noeuds entre eux avec le poids minimal possible.

Je proposerai donc à Fanchon Bergeron des itenerraires aléatoires qui lui permettront de parcourir les pays et les continents.


### 2.3 - La globe trotteuse

Choix d'algorithme: Closeness Centrality.

Cet algorithme mesure la centralité d'un nœud par rapport à tous ses voisins au sein de son cluster. 
Les nœuds (aéroports = villes) ayant les chemins les plus courts vers tous les autres nœuds sont supposés pouvoir atteindre l'ensemble du groupe le plus rapidement.

En trouvant les noeuds les plus accéssibles aux autres noeuds, je pourrai proposer une liste des villes auxquelles Estelle Chauvet pourra deménager et qui lui permettra de pratiquer sa passion de voyage ainsi qu'elle retournera chez elle à chaque fois.


### 2.4 - Les indispensables

Choix d'algorithme: Betweenness Centrality.

Pour répondre au problème des aéroports indispensables je passe par l'algorithme de centralité d'intermédiarité,
qui mesure le nombre de chemins les plus courts qui passent par un nœud (aéroport). Les nœuds qui se trouvent le plus souvent sur les chemins les plus courts ont des scores de centralité d'interdépendance plus élevés. 

Je pourrai donc proposer à Michel Sabourin la liste des aéroports critiques classés par leur score de centralité d'interdépendance (= la criticité) descendant.


### 2.5 - Les interconnectés

c'est fait.
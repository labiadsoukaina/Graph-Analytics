# Graph-Analytics

### 2.1 - Le voyageur du Monde
 
Choix de l’algorithme : All-Pairs Shortest Paths.
 
### 2.2 - La fainéantise du voyageur
 
Choix de l’algorithme : Minimum Weight Spanning Tree.
 
Il s'agit ici d'un problème de marche aléatoire qu'on peut résoudre en utilisant l'algorithme "Minimum Weight Spanning Tree", qui cherche à partir d'un nœud donné (aéroport de départ) tous les nœuds atteignables (aéroports de destination) ainsi que l'ensemble des relations qui relient les nœuds entre eux avec le poids minimal possible.
 
Je proposerai donc à Fanchon Bergeron des itinéraires aléatoires qui lui permettront de parcourir les pays et les continents.
 
 
### 2.3 - La globe trotteuse
 
Choix de l’algorithme : Closeness Centrality.
 
Cet algorithme mesure la centralité d'un nœud par rapport à tous ses voisins au sein de son cluster.
Les nœuds (aéroports = villes) ayant les chemins les plus courts vers tous les autres nœuds sont supposés pouvoir atteindre l'ensemble du groupe le plus rapidement.
 
En trouvant les nœuds les plus accessibles aux autres nœuds, je pourrai proposer une liste des villes auxquelles Estelle Chauvet pourra déménager et qui lui permettra de pratiquer sa passion de voyage ainsi qu'elle retournera chez elle à chaque fois.
 
 
### 2.4 - Les indispensables
 
Choix de l’algorithme : Betweenness Centrality.
 
Pour répondre au problème des aéroports indispensables je passe par l'algorithme de centralité d'intermédiarité, qui mesure le nombre de chemins les plus courts qui passent par un nœud (aéroport). Les nœuds qui se trouvent le plus souvent sur les chemins les plus courts ont des scores de centralité d'interdépendance plus élevés.
 
Je pourrai donc proposer à Michel Sabourin la liste des aéroports critiques classés par leur score de centralité d'interdépendance (= la criticité) descendant.
 
 
### 2.5 - Les interconnectés
 
Choix de l’algorithme : All-Pairs Shortest Paths.

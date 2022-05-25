import sys
import pandas as pd
 
class Graph(object):
    print("Voyageur du Monde Start !")
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
            
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path

def get_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)

    distance_chemin = shortest_path[target_node]
    chemin = " -> ".join(reversed(path))

    return chemin, distance_chemin
    # print("We found the following best path with a value of {}.".format(distance_chemin))
    # print(chemin)

def generate_graph_from_csv():
    data = pd.read_csv("voyageur_monde_FV")
    df = pd.DataFrame(data)

    airports_source_list = df['source'].tolist()
    airports_target_list = df['target'].tolist()
    airports_list = airports_source_list + airports_target_list

    airports_list = list(dict.fromkeys(airports_list))

    init_graph = {}
    for airport in airports_list:
        init_graph[airport] = {}

    for index, row in df.iterrows():
        source = row["source"]
        target = row["target"]
        distance = row["distance"]
        init_graph[source][target] = distance
    
    return airports_list, init_graph

def airports_non_lies(airport_depart):
    data = pd.read_csv("voyageur_monde_FV")
    df = pd.DataFrame(data)
    lis, graph = generate_graph_from_csv()
    lis.remove(airport_depart)
    
    for index, row in df.iterrows():
        if row["source"] ==airport_depart:
            lis.remove(row["target"])
    # print(lis)
    return lis

def start_process(start_airport, target_airport):
    nodes, init_graph = generate_graph_from_csv()
    graph = Graph(nodes, init_graph)

    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_airport)
    chemin, distance_chemin = get_result(previous_nodes, shortest_path, start_node=start_airport, target_node=target_airport)
    print(chemin)
    print(distance_chemin)
    return chemin, distance_chemin
#aller
start_process("Toulouse-Blagnac Airport","Halmstad Airport")
#retour
start_process("Halmstad Airport","Košice Airport") 
start_process("Košice Airport","Toulouse-Blagnac Airport")




# start_airport = "Toulouse-Blagnac Airport"
# list_airports_non_lies = airports_non_lies(start_airport)
# result = []

# print(list_airports_non_lies)
# for airport_non_lie in list_airports_non_lies:
#     chemin, distance_chemin = start_process(start_airport, airport_non_lie)
#     result.append(distance_chemin)
# print(result)


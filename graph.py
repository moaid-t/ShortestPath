from ShortestPath import ShortestPath
import networkx as nx
import matplotlib.pyplot as plt

Graph = nx.Graph()

#  input
len_of_node = int(input("Number Of Node : "))
for i in range(1, len_of_node + 1):
    Graph.add_node(i)

print("Note : Enter '0' Number If Their No Edge Between Two Node ")
for i in range(1, len_of_node + 1):
    k = (len_of_node - i)
    for j in range(1, k + 1):
        j += i
        weight = int(input(f"the weight of '{i}' <-?-> '{j}' : "))
        if weight != 0:
            Graph.add_edge(i, j, color='black', weight=weight)

start_point = int(input("The start point is --> "))
end_point = int(input("The end point is --> "))
# /input


# Graph style
pos = nx.random_layout(Graph)
Graph2 = Graph.copy()

label = nx.get_edge_attributes(Graph, 'weight')
colors = nx.get_edge_attributes(Graph, 'color').values()
# /Graph style

# apply alg
get_path = ShortestPath(label, len_of_node, start_point, end_point)
get_path.find()
short_path = get_path.get_short_paths()
e_cost = get_path.get_cost()

print(label)

ph = ''
for i in short_path:
    if i == end_point:
        ph += str(i)
    else:
        ph += f'{i}-->'


color_map = []
for node in Graph:
    if node in short_path:
        color_map.append('green')
    else:
        color_map.append('red')

plt.figure(1)
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=label, font_size=10)
nx.draw(Graph, pos, with_labels=True, edge_color=colors, node_color=color_map)
plt.title(f"Solution  Graph\nShortest Path: {ph} With Cost: {e_cost}", size=10)

plt.figure(2)
nx.draw_networkx_edge_labels(Graph2, pos, edge_labels=label, font_size=10)
nx.draw(Graph2, pos, with_labels=True, edge_color=colors)
plt.title("Original  Graph")

plt.show()

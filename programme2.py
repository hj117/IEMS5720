import pandas as pd
import networkx as nx

dimension = 75
ID = 15

df = pd.read_csv("Social_Matrix.csv")
matrix = df.values

u_graph = nx.DiGraph()
u_graph.add_nodes_from(range(1, dimension + 1))

for i in range(len(matrix[0])):
	for j in range(len(matrix)):
		if matrix[j][i] == 1:
			u_graph.add_edge(j + 1, i + 1)

print("In degree:")
print(u_graph.in_degree(ID))
print("Out degree:")
print(u_graph.out_degree(ID))
print("closeness centrality:")
print(nx.closeness_centrality(u_graph, ID))
print("betweenness centrality:")
print(nx.betweenness_centrality(u_graph)[ID])

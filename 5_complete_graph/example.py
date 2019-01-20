from graphviz import Graph


N = int(input('Enter edge count: '))

graph = Graph('example',  format='svg', engine='circo')

for i in range(1, N+1):
    for j in range(i+1, N+1):
        graph.edge(str(i), str(j))

graph.view()
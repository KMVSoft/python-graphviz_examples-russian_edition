from graphviz import Digraph

g = Digraph('example', format='svg')

list_of_nodes = ['Пришёл', 'Увидел', 'Победил']

for i in range(len(list_of_nodes) - 1):
    g.edge(list_of_nodes[i], list_of_nodes[i+1])

g.view()

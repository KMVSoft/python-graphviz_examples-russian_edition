from graphviz import Digraph


graph = Digraph('example',  format='svg', engine='circo')

graph.node('1', label='Украл')
graph.node('2', label='Выпил')
graph.node('3', label='В тюрьму')

graph.edge('1', '2')
graph.edge('2', '3')
graph.edge('3', '1')

graph.view()
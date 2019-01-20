from graphviz import Graph

class Node():
    '''Простой класс, который содержит информацию 
    об узле графа'''
    def __init__(self, text, color):
        self.text = text
        self.color = color

graph = Graph('example',  format='svg')

nodes = [
    Node('Каждый', 'red'),
    Node('Охотник', 'orange'),
    Node('Желает', 'yellow'),
    Node('Знать', 'green'),
    Node('Где', 'cyan'),
    Node('Сидит', 'blue'),
    Node('Фазан', 'purple'),
]

for node in nodes:
    graph.node(
        node.text,
        color=node.color,
        style='filled',
        width='2'
    )

for i in range(len(nodes) - 1):
    graph.edge(
        nodes[i].text,
        nodes[i+1].text,
    )

graph.view()
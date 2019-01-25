import random
from graphviz import Graph
  

def get_rand_color(min=50, max=200):
    color = tuple(random.randint(min, max) for c in ('r', 'g', 'b')) 
    return '#%0.2X%0.2X%0.2X' % color

def degree_of(node, matrix):
    '''Степень узла неориентированного графа'''
    degree = 0
    for edge in matrix[node]:
        degree += (1 if edge else 0)
    return degree

def get_rand_graph(node_count, node_degree=3):
    adjacency_matrix = [
        [0 for i in range(node_count)] for j in range(node_count)
    ]
    for node, edges in enumerate(adjacency_matrix):
        available_nodes = [i for i in range(node+1, node_count)]
        i = node_degree-sum(edges)

        while i:
            if not available_nodes: break 
            c = random.choice(available_nodes)
            degree = degree_of(c, adjacency_matrix)
            if degree < node_degree:
                adjacency_matrix[node][c] = adjacency_matrix[c][node] = 1
                i -= 1
            available_nodes.remove(c)
    return adjacency_matrix

def draw_multicolored_graph(adjacency_matrix):
    graph = Graph('example', engine='dot', format='svg')
    for node, edges in enumerate(adjacency_matrix):
        graph.node(str(node), color=get_rand_color(), style='filled')
        for neigbor, edge in enumerate(edges[:node]):
            if edge:
                graph.edge(str(node), str(neigbor))
    graph.view()


if __name__=='__main__':
    draw_multicolored_graph(get_rand_graph(30, node_degree=3))


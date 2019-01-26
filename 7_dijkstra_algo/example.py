import random
import bisect
from collections import deque
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


def dijkstra_index(index_node, matrix, distance, visited):
    visited.add(index_node)
    neigbors = []

    for node, edge in enumerate(matrix[index_node]):
        if edge and node not in visited:
            if distance[index_node] + edge < distance[node]:
                distance[node] = distance[index_node] + edge

            bisect.insort(neigbors, (edge, node))

    return neigbors


def dijkstra(matrix, start_node):
    'Реализация алгоритма Дейкстры'

    # Начальная инициализация
    # Задаём всем вершинам расстояние - бесконечность
    distance = [float("inf")]*len(matrix)
    # Расстояние до начальной вершины уже известно - 0
    distance[start_node] = 0
    visited = set()

    queue = deque()
    queue.append(dijkstra_index(start_node, matrix, distance, visited))
    
    while queue:
        nodes = queue.popleft()
        for edge, node in nodes:
            neigbors = dijkstra_index(node, matrix, distance, visited)
            if neigbors:
                queue.append(neigbors)
    
    return distance


def shortest_path(matrix, distance, to_node):
    '''Выдаёт кратчайший путь от вершины node до
    узла начала алгоритма Дейкстры
    :result: [(node, x), (x, y), .., (b, a)] 
    '''
    if distance[to_node] == float('inf'): return []
    path = []
    start_node = distance.index(0)
    while to_node != start_node:
        min_dist = float('inf')
        min_node = None
        for node, edge in enumerate(matrix[to_node]):
            if edge and distance[node] < min_dist:
                min_dist = distance[node]
                min_node = node
        path.append((min_node, to_node))
        to_node = min_node
    return path

def draw_graph(adjacency_matrix, path):
    graph = Graph('example', engine='dot', format='svg')
    for node, edges in enumerate(adjacency_matrix):
        graph.node(str(node), color=get_rand_color(), style='filled')
        for neigbor, edge in enumerate(edges[:node]):
            if edge:
                graph.edge(
                    str(node),
                    str(neigbor),
                    color=('red' if (node, neigbor) in path
                                 or (neigbor, node) in path
                                 else 'black')
                )

    graph.view()

if __name__=='__main__':
    node_count = 40
    matrix = get_rand_graph(node_count, node_degree=3)
    distance = dijkstra(matrix, 0)
    the_farthest_node = distance.index(max(distance))
    path = shortest_path(matrix, distance, the_farthest_node)
    draw_graph(matrix, path)
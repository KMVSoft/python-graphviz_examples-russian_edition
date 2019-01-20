from graphviz import Graph

class Node():
    '''Описывает узел бинарного дерева'''
    def __init__(self, text):
        self.text = text
        self.no = None
        self.yes = None

    def setNo(self, node):
        self.no = node

    def setYes(self, node):
        self.yes = node


root = Node('Это двигается?')
node1 = Node('А должно ?')
node2 = Node('А должно?')
root.setNo(node1)
root.setYes(node2)
node3 = Node('Тогда всё в порядке')
node4 = Node('Спрыкай WD-40')
node1.setNo(node3)
node1.setYes(node4)
node5 = Node('Фигачь синей изолентой')
node6 = Node('Не ссы, всё в порядке')
node2.setNo(node5)
node2.setYes(node6)


def createTree(node, graph):
    if node.no is not None:
        graph.edge(node.text, node.no.text, label='Нет')
        createTree(node.no, graph)
    if node.yes is not None:
        graph.edge(node.text, node.yes.text, label='Да')
        createTree(node.yes, graph)

graph = Graph('example',  format='svg')
createTree(root, graph)
graph.view()
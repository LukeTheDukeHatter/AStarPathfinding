class Node():
    def __init__(self):
        self.Visited = False
        self.Right = False
        self.Down = False

    def visit(self):
        self.Visited = True

class Maze():
    def __init__(self, width, height):
        self.Graph = [[Node() for x in range(width)] for x in range(height)]
        
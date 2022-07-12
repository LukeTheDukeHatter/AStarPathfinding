
AJL = {
    'A':['B','C'],
    'B':['D','A','C'],
    'C':['B','A'],
    'D':['B']
}


class Path():
    def __init__(self, path:list, cost:int):
        self.Route = path
        self.Cost = cost

    def AddStep(self,point:str,cost:int):
        self.Route.append(point)
        self.Cost += cost

    def copy(self):
        return self

def AStar(Graph, Start, End):
    Weights = {
        0:[Path([Start])]
    }
    Correct = {}
    

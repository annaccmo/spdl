from spdl import modelCheck as modelCheck

#actions
class Stack:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.preCond = {'Clear'+str(x), 'Clear'+str(y)}
        self.addCond = {str(y)+'On'+str(x)}
        self.delCond = {'Clear'+str(x), str(y)+'onTable'}
        self.name = 'Stack'

    def equal (self, obj):
        if type(obj) == Stack:
            if (self.x == obj.x) and (self.y == obj.y):
                return True
            else:
                return False
        else:
            return False

    def conditions (self):
        cond = {'action': self.name, 'pre': self.preCond, 'add': self.addCond, 'del': self.delCond}
        return cond


class Unstack:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.preCond = {str(x)+'On'+str(y), 'Clear'+str(x)} 
        self.addCond = {str(x)+'onTable', 'Clear'+str(y)}
        self.delCond = {str(x)+'On'+str(y)} 
        self.name = 'Unstack'

    def equal (self, obj):
        if type(obj) == Unstack:
            if (self.x == obj.x) and (self.y == obj.y):
                return True
            else:
                return False
        else:
            return False

    def conditions (self):
        cond = {'action': self.name, 'pre': self.preCond, 'add': self.addCond, 'del': self.delCond}
        return cond

stackAB = Stack('A','B')
stackBA = Stack('B','A')
stackAC = Stack('A','C')
stackCA = Stack('C','A')
stackBC = Stack('B','C')
stackCB = Stack('C','B')

unstackAB = Unstack('A','B')
unstackBA = Unstack('B','A')
unstackAC = Unstack('A','C')
unstackCA = Unstack('C','A')
unstackBC = Unstack('B','C')
unstackCB = Unstack('C','B')

actions = [stackAB.conditions(), stackBA.conditions(), stackAC.conditions(), stackCA.conditions(), stackBC.conditions(), stackCB.conditions(), unstackAB.conditions(), unstackBA.conditions(), unstackAC.conditions(), unstackCA.conditions(), unstackBC.conditions(), unstackCB.conditions()]


#Initial State
initialState = {'AonTable', 'BonTable', 'ClearA', 'ClearB', 'ClearC'}

#Final State
finalState = {'AonTable', 'BOnA', 'COnB', 'ClearC'}

#Model Checking
s,a = modelCheck (initialState, finalState, actions)

print("States:  \n\t"+str(s)+"\n\n"+"Actions:  \n\t"+str(a))


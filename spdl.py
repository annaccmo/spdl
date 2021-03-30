'''
initialState -> set
finalState -> set
action -> list -> [{'pre': set, 'add': set, 'del': set}]
'''
def modelCheck (initialState, finalState, actions):

    if finalState != initialState:
        actual = finalState
        
        #difStates = (finalState - initialState) | (initialState - finalState)

    statesStack = []
    actionStack = []
    i = 0
    while True: #Pensar numa condição de parada
        for a in actions:
            if a['add'] <= actual and ((a['del'] & actual) == set()):
                newState = (actual - a['add']) | a['del'] 
                if a['pre'] <= newState and not(newState in statesStack):
                    #difNew = (newState - initialState) | (initialState - newState)
                    #if difStates > difNew:
                    actual = newState
                    actionStack.append(a)
                    if (newState <= initialState) or (initialState <= newState):#faz sentido essa condição?
                        return statesStack, actionStack
                    i=0
                else:
                    i+=1
            else:
                i+=1
        if i>len(actions):
            break

        statesStack.append(actual)

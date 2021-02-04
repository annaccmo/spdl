'''
initialState -> set
finalState -> set
action -> list -> [{'pre': set, 'add': set, 'del': set}]
'''
def modelCheck (initialState, finalState, actions):

    if finalState != initialState:
        actual = finalState
        
        difStates = (finalState - initialState) | (initialState - finalState)

    statesStack = []
    while True: #Pensar numa condição de parada
        for a in actions:

            if a['add'] <= actual and ((a['del'] & actual) == set()):
                newState = (actual - a['add']) | a['del']
                if a['pre'] <= newState and not(newState in statesStack):
                    difNew = (newState - initialState) | (initialState - newState)
                    if difStates > difNew:
                        actual = newState
                        if (newState <= initialState) or (initialState <= newState):#faz sentido essa condição?
                            return statesStack

        statesStack.append(actual)

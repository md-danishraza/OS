
def BankerAlgorithm(allocMatrix,maxMatrix,availableMatrix):
    Processes = list(allocMatrix.keys())

    # print(Processes)
    # Number of processes
    n = len(allocMatrix)
    # safesequence list
    safeSeq = []

    # calculate need matrix
    needMatrix = {}
    for process in Processes:
        needMatrix[process] = [maxMatrix[process][i] - allocMatrix[process][i] for i in range(3)]


    flag = 0
    print(needMatrix)

    while len(safeSeq) != n:
        if flag == n:
            print('System is in unsafe state')
            break
        # find a process which has all resources available
        for process in Processes:
            if all(need <= availableMatrix[i] for i, need in enumerate(needMatrix[process])):
                safeSeq.append(process)
                # increase available resources
                availableMatrix = [availableMatrix[i] + allocMatrix[process][i] for i in range(3)]

                
                # Remove the process from the list
                Processes.remove(process)
                # reset flag
                flag = 0
            else:
                flag += 1
                

    return safeSeq


if __name__ == '__main__':
    # Available resources
    available = [3, 3, 2]
    # Maximum resource allocation for processes
    maxMatrix = {
        'P0':[7, 5, 3],
        'P1':[3, 2, 2],
        'P2':[9, 0, 2],
        'P3':[2, 2, 2],
        'P4':[4, 3, 3],
        'P5':[6, 3, 4]
    }
    # Current allocation of resources for processes
    allocMatrix = {
        'P0': [0, 1, 0],
        'P1': [2, 0, 0],
        'P2': [3, 0, 2],
        'P3': [2, 1, 1],
        'P4': [0, 0, 2],
        'P5': [1, 0, 0]
    }
    # Available resources
    available2 = [3, 3, 2]
    # Maximum resource allocation for processes
    maxMatrix2 = {
        'P0':[7, 5, 3],
        'P1':[3, 2, 2],
        'P2':[9, 0, 2],
        'P3':[2, 2, 2],
        'P4':[4, 3, 3],
    }
    # Current allocation of resources for processes
    allocMatrix2 = {
        'P0': [0, 1, 0],
        'P1': [2, 0, 0],
        'P2': [3, 0, 2],
        'P3': [2, 1, 1],
        'P4': [0, 0, 2],

    }

    safeSeq = BankerAlgorithm(allocMatrix2, maxMatrix2, available2)
    print('Safe sequence is:', safeSeq)


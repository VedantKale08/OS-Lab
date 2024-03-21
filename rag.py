def is_safe_state(available, rem_need, finished):
    work = available.copy()
    finish = finished.copy()

    while True:
        found = False
        for i in range(no_of_processes):
            if not finish[i]:
                if all(rem_need[i][j] <= work[j] for j in range(no_of_resources)):
                    for j in range(no_of_resources):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    found = True
        if not found:
            break
    
    return all(finish)

if __name__ == '__main__':
    no_of_processes = 5
    no_of_resources = 3
    total = [10, 5, 7]
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    available = [3, 3, 2]
    rem_need = [[0] * no_of_resources for _ in range(no_of_processes)]

    for i in range(no_of_processes):
        for j in range(no_of_resources):
            rem_need[i][j] = max_need[i][j] - allocation[i][j]

    finished = [False] * no_of_processes

    if is_safe_state(available, rem_need, finished):
        print("System is in safe state (No Deadlock detected)\n")
    else:
        print("System is in an unsafe state (Deadlock detected)")

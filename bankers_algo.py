def display_table():
    print("Process |\t Allocation \t|\t Max Need \t|\t Remaining Need |")
    print("--------+-----------------------+-----------------------+-----------------------+")
    for i in range(no_of_processes):
        print(f"P{i} \t|\t {allocation[i]} \t|\t {max_need[i]} \t|\t {rem_need[i]} \t|")

if __name__ == '__main__':
    no_of_processes = 5
    no_of_resources = 3
    total = [10,5,7]
    allocation = [
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2]
    ]
    max_need = [
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2],
        [4,3,3]
    ]
    available = [3,3,2]
    rem_need = [[0] * no_of_resources for _ in range(no_of_processes)]
    safe_seq = []

    for i in range(no_of_processes):
        for j in range(no_of_resources):
            rem_need[i][j] = max_need[i][j] - allocation[i][j]

    finished = [False] * no_of_processes

    for _ in range(no_of_processes):
        for i in range(no_of_processes):
           if not finished[i]:
               count = 0
               
               for j in range(no_of_resources):
                   if rem_need[i][j] <= available[j]:
                       count+=1

               if count == no_of_resources:
                   safe_seq.append(f"P{i+1}")
                   for j in range(no_of_resources):
                       available[j] += allocation[i][j]
                   finished[i] = True

    if len(safe_seq) == no_of_processes:
        print("System is in safe state\n")
        display_table()
        print("\nSafe Sequence : ", safe_seq)
    else:
        print("System is in an unsafe state")
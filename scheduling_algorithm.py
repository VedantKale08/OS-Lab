import matplotlib.pyplot as plt
import numpy as np

arrival_time = []
burst_time = []



def first_come_first_serve():
    print("First serve algorithm")
    completion_time = [0]*len(arrival_time)
    waiting_time = [0]*len(arrival_time)
    turnaround_time = [0]*len(arrival_time)

    completion_time[0] = burst_time[0];
    for i in range(1, len(arrival_time)):
        completion_time[i] = max(completion_time[i-1] + burst_time[i], 0)

    total_turnaround_time = 0    
    total_waiting_time = 0

    for i in range(len(arrival_time)):
        turnaround_time[i] = max(completion_time[i] - arrival_time[i], 0)  #completion_time[i] - arrival_time[i] is turnaround time
        waiting_time[i] = max(turnaround_time[i] - burst_time[i],0)    #turnaround time - burst_time[i] is waiting time
        total_turnaround_time += turnaround_time[i]
        total_waiting_time += waiting_time[i]
    
    average_waiting_time = total_waiting_time / len(arrival_time)
    average_turnaround_time = total_turnaround_time / len(arrival_time)


    print("Process \t Arrival time \t Burst time \t Completion time \t Turnaround time \t waiting time")
    for i in range(len(arrival_time)):  
        print(f"{i+1}\t\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"\nAverage Turn Around Time: {average_turnaround_time}")

    plt.figure(figsize=(10, 2))
    colors = np.random.rand(len(arrival_time), 3)
    for i in range(len(arrival_time)):
        plt.barh(y=0, width=burst_time[i], left=max(completion_time[i] - burst_time[i], arrival_time[i]), color=colors[i], align='center', edgecolor='black')
        plt.text(max(completion_time[i] - burst_time[i], arrival_time[i]) + burst_time[i] / 2, 0, f"P{i+1}", ha='center', va='center', color='white')

    plt.title('Gantt Chart - FCFS')
    plt.xlabel('Time')
    plt.yticks([])
    plt.show()




def shortest_job_first():
    print("Shortest job first")

    while True:
        print("\nChoose one algorithm : ")
        print("1. Preemptive ")
        print("2. Non Preemptive")
        print("3. Exit")

        ch = int(input("Enter algorithm No : "))

        match ch:
            case 1 :
                sjf_preemptive()
            case 2 :
                sjf_non_preemptive()
            case 3 :
                break
            case _:
                print("Algorithm not found")
                break




def sjf_preemptive():
    print("Preemptive")

    switch_time = int(input("Enter switch time : "))

    n = len(arrival_time)
    remaining_time = burst_time.copy()
    completion_time = [0] * n
    waiting_time = [0]* n
    turnaround_time = [0]* n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    process_sequence = []

    while True:
        shortest_job = None
        shortest_time = float('inf')

        for i in range(n):
            if(arrival_time[i] <= current_time and remaining_time[i] < shortest_time and remaining_time[i] > 0):
                shortest_job = i
                shortest_time = remaining_time[i]
        
        if shortest_job is None:
            break

        process_sequence.append(shortest_job + 1)
        remaining_time[shortest_job] -= switch_time

        if remaining_time[shortest_job] == 0 :
            completion_time[shortest_job] = current_time
            turnaround_time[shortest_job] = completion_time[shortest_job] - arrival_time[shortest_job]
            waiting_time[shortest_job] = turnaround_time[shortest_job] - burst_time[shortest_job]
            total_waiting_time += waiting_time[shortest_job]
            total_turnaround_time += turnaround_time[shortest_job]
        
        current_time += switch_time

    average_turnaround_time = total_turnaround_time/n
    average_waiting_time = total_waiting_time/n

    print("Process \t Arrival time \t Burst time \t Completion time \t Turnaround time \t waiting time")
    for i in range(len(arrival_time)):  
        print(f"{i+1}\t\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"\nAverage Turn Around Time: {average_turnaround_time}")

    colors = plt.cm.viridis(np.linspace(0, 1, n))

    plt.figure(figsize=(10, 1.5))
    for i,process in enumerate(process_sequence):
        plt.barh(0, switch_time, left=i * switch_time, color=colors[process-1], align='center', edgecolor='black')
        plt.text(i * switch_time + switch_time / 2, 0, f'P{process_sequence[i]}', ha='center', va='center', color='white')
    plt.xlim(0, len(process_sequence) * switch_time) 
    plt.ylim(-0.5, 0.5)
    plt.yticks([])
    plt.title('Gantt Chart - Round Robin Scheduling')
    plt.xlabel('Time')
    plt.show()





def sjf_non_preemptive():
    print("Non Preemptive")
    n = len(arrival_time)
    remaining_time = burst_time.copy()
    completion_time = [0] * n
    waiting_time = [0]* n
    turnaround_time = [0]* n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    while True:
        shortest_job = None
        shortest_time = float('inf')

        for i in range(n):
            if(arrival_time[i] <= current_time and remaining_time[i] < shortest_time and remaining_time[i] > 0):
                shortest_job = i
                shortest_time = remaining_time[i]
        
        if shortest_job is None:
            break

        current_time += remaining_time[shortest_job]
        completion_time[shortest_job] = current_time
        remaining_time[shortest_job] = 0
        turnaround_time[shortest_job] = completion_time[shortest_job] - arrival_time[shortest_job]
        waiting_time[shortest_job] = turnaround_time[shortest_job] - burst_time[shortest_job]
        total_waiting_time += waiting_time[shortest_job]
        total_turnaround_time += turnaround_time[shortest_job]

    average_turnaround_time = total_turnaround_time/n
    average_waiting_time = total_waiting_time/n

    print("Process \t Arrival time \t Burst time \t Completion time \t Turnaround time \t waiting time")
    for i in range(len(arrival_time)):  
        print(f"{i+1}\t\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"\nAverage Turn Around Time: {average_turnaround_time}")
    
    plt.figure(figsize=(10, 2))
    colors = np.random.rand(len(arrival_time), 3)
    for i in range(len(arrival_time)):
        plt.barh(y=0, width=burst_time[i], left=max(completion_time[i] - burst_time[i], arrival_time[i]), color=colors[i], align='center', edgecolor='black')
        plt.text(max(completion_time[i] - burst_time[i], arrival_time[i]) + burst_time[i] / 2, 0, f"P{i+1}", ha='center', va='center', color='white')

    plt.title('Gantt Chart - Priority')
    plt.xlabel('Time')
    plt.yticks([])
    plt.show()




def round_robin():
    print("Round Robin Algorithm")
    n = len(arrival_time)
    remaining_time = burst_time.copy()
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    process_sequence = []  # to store the sequence of processes executed

    time_slice = int(input("Enter time slice: "))

    while True:
        all_processes_completed = True
        for i in range(n):
            if remaining_time[i] > 0:
                all_processes_completed = False
                process_sequence.append(i + 1)  # Append process number to the sequence
                if remaining_time[i] > time_slice:
                    current_time += time_slice
                    remaining_time[i] -= time_slice
                else:
                    current_time += remaining_time[i]
                    remaining_time[i] = 0
                    completion_time[i] = current_time
                    turnaround_time[i] = completion_time[i] - arrival_time[i]
                    waiting_time[i] = turnaround_time[i] - burst_time[i]
                    total_waiting_time += waiting_time[i]
                    total_turnaround_time += turnaround_time[i]

        if all_processes_completed:
            break

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print("Process \t Arrival time \t Burst time \t Completion time \t Turnaround time \t Waiting time")
    for i in range(len(arrival_time)):
        print(f"{i+1}\t\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"\nAverage Turnaround Time: {average_turnaround_time}")

    colors = plt.cm.viridis(np.linspace(0, 1, n))

    # Plotting Gantt Chart
    plt.figure(figsize=(10, 1.5))
    for i, process in enumerate(process_sequence):
        plt.barh(0, time_slice, left=i * time_slice, color=colors[process-1], align='center', edgecolor='black')
        plt.text(i * time_slice + time_slice / 2, 0, f'P{process}', ha='center', va='center', color='white')
    plt.xlim(0, len(process_sequence) * time_slice) 
    plt.ylim(-0.5, 0.5)
    plt.yticks([])
    plt.title('Gantt Chart - Round Robin Scheduling')
    plt.xlabel('Time')
    plt.show()


def priority_algo():
    print("Priority Based Algorithm")
    n = len(arrival_time)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    priority = []

    for i in range(n):
        priority.append(int(input(f"Enter Priority of P{i+1} : ")))
    
    processes = list(range(n))
    processes.sort(key=lambda x: priority[x], reverse=True)

    for i in processes:
        current_time = max(current_time, arrival_time[i])
        completion_time[i] = current_time + burst_time[i]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        current_time = completion_time[i]

    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n

    print("Process \t Arrival time \t Burst time \t Priority \t Completion time \t Turnaround time \t Waiting time")
    for i in range(n):
        print(f"{i+1}\t\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {priority[i]}\t\t {completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turn Around Time: {average_turnaround_time}")

    plt.figure(figsize=(10, 2))
    colors = np.random.rand(len(arrival_time), 3)
    for i in range(len(arrival_time)):
        plt.barh(y=0, width=burst_time[i], left=max(completion_time[i] - burst_time[i], arrival_time[i]), color=colors[i], align='center', edgecolor='black')
        plt.text(max(completion_time[i] - burst_time[i], arrival_time[i]) + burst_time[i] / 2, 0, f"P{i+1}", ha='center', va='center', color='white')

    plt.title('Gantt Chart - Priority')
    plt.xlabel('Time')
    plt.yticks([])
    plt.show()




if __name__ == "__main__":

    noOfProcess = int(input("Enter number of processes : "))

    for index in range(noOfProcess):
        print("\nProcess no ",index+1)
        arrival_time.append(int(input("Enter Arrival time : ")))
        burst_time.append(int(input("Enter Burst time : ")))
    
    while True:
        print("\nChoose one algorithm : ")
        print("1. First come First Serve Algorithm")
        print("2. Short job first Algorithm")
        print("3. Round Robin Algorithm")
        print("4. Priority based Algorithm")
        print("5. Exit")

        option = int(input("Enter algorithm No : "))

        match option:
            case 1 :
                first_come_first_serve()
            case 2 :
                shortest_job_first()
            case 3 :
                round_robin()
            case 4 :
                priority_algo()
            case 5 :
                print("Exiting")
                break
            case _:
                print("Algorithm not found")
                break

import threading
import random
import time

def acquire(semaphore):
    with semaphore['cv']:
        while semaphore['s'] >= semaphore['max_allowed']:
            semaphore['cv'].wait()
        semaphore['s'] += 1

def release(semaphore):
    with semaphore['cv']:
        semaphore['s'] -= 1
        semaphore['cv'].notify_all()

def process_function(semaphore, pid, execution_time, count, num_allowed):
    if count > num_allowed:
        print(f"P{pid} blocked")
    acquire(semaphore)
    print(f"P{pid} enters in Critical Section")
    time.sleep(execution_time)
    print(f"P{pid} coming out of Critical Section")
    release(semaphore)

if __name__ == "__main__":
    num_processes = int(input("Enter number of processes: "))

    execution_times = [random.randint(1, 10) for _ in range(num_processes)]
    print(execution_times)
    
    while True:
        print("\nChoose Type: ")
        print("1. Binary Semaphore")
        print("2. Counting Semaphore")
        print("Choose any option to exit")

        num_allowed = 1

        option = input("Enter Type : ")
        if option == "1":
            semaphore = {'max_allowed': 1, 's': 0, 'cv': threading.Condition()}
        elif option == "2":
            num_allowed = int(input("Enter number of processes allowed in critical section: "))
            semaphore = {'max_allowed': num_allowed, 's': 0, 'cv': threading.Condition()}
        else:
            print("Exiting...")
            break

        processes = []
        count = 1

        for i in range(num_processes):
            t = threading.Thread(target=process_function, args=(semaphore, i+1, execution_times[i], count, num_allowed))
            count += 1
            processes.append(t)

        for t in processes:
            t.start()

        for t in processes:
            t.join()

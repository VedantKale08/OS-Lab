import threading

shared_resource = 5

lock = threading.Lock()

def increment():
    global shared_resource
    for _ in range(1000):
        lock.acquire()
            # critical section
        shared_resource = shared_resource + 1
        lock.release()

def decrement():
    global shared_resource
    for _ in range(1000):
        lock.acquire()
            # critical section
        shared_resource = shared_resource - 1
        lock.release()

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final value of shared_resource:", shared_resource)
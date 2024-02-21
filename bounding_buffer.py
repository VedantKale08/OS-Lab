import time
import random

def producer():
    if len(buffer) >= buffer_size:
        print("Producer found buffer full")
    else:
        item = random.randint(1, 10)
        buffer.append(item)
        print(f"Producer produced item {item}")
        time.sleep(0.5)

def consumer():
    if len(buffer) == 0:
        print("Consumer found buffer empty")
    else:
        item = buffer.pop(0)
        print(f"Consumer consumed item {item}")
        time.sleep(0.5)

if __name__ == "__main__":
    buffer = []
    buffer_size = int(input("Enter the size of the buffer : "))

    while True:
        # print(buffer)
        if random.choice([True,False]):
            producer()
        else:
            consumer()
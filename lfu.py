from collections import defaultdict

def lfu(page_references_string, frames_count):
    page_frequency = defaultdict(int)
    last_used_time = {}
    frames = []
    page_fault = 0
    hit = 0
    frameMatrix = [['-' for _ in range(len(page_references_string))] for _ in range(frames_count)]
    statusArray = []

    for j, page in enumerate(page_references_string):
        page_frequency[page] += 1
        last_used_time[page] = j
        
        if page not in frames:
            page_fault += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                least_frequent = min(frames, key=lambda x: (page_frequency[x], last_used_time[x]))
                frames[frames.index(least_frequent)] = page
            statusArray.append("Miss")
        else:
            hit += 1
            statusArray.append("Hit")

        for i, frame in enumerate(frames):
            frameMatrix[i][j] = frame

    print("Frames :")
    for row in frameMatrix:
        for item in row:
            print("|   " + str(item) + "   ", end="")
        print()
    print(statusArray)
    print(f"\nHit : {hit}")
    print(f"Page Faults : {page_fault}")

if __name__ == "__main__":
    page_references_string = [5, 0, 1, 3, 2, 4, 1, 0, 5]
    frames_count = 4
    lfu(page_references_string, frames_count)

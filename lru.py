def lru(page_references_string, frames_count):
    frames = []
    page_fault = 0
    hit = 0
    frameMatrix = [['-' for _ in range(len(page_references_string))] for _ in range(frames_count)]
    statusArray = []

    for j, page in enumerate(page_references_string):
        if page not in frames:
            page_fault += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                least_recently_used = min(range(frames_count), key=lambda x: page_references_string.index(frames[x]))
                frames[least_recently_used] = page
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
    page_references_string = [1, 3, 0, 3, 5, 6, 3, 4, 1, 3, 5, 6, 3]
    frames_count = 4
    lru(page_references_string, frames_count)

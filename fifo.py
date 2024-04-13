def fifo(page_references_string, frames_count):
    frames = []
    page_fault = 0
    hit = 0
    index = 0
    frameMatrix = [['-' for i in range(len(page_references_string))] for j in range(frames_count)]
    statusArray = []

    j = 0
    for page in page_references_string:
        if page not in frames:
            page_fault += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1)%frames_count
            statusArray.append("Miss")
        else:
            hit += 1
            statusArray.append("Hit")

        for i in range(len(frames)):
            frameMatrix[i][j] = frames[i]
        j+=1


    print("Frames :")
    for row in frameMatrix:
        for item in row:
            print("|   " + str(item) + "   ", end="")
        print()
    print(statusArray)
    print(f"\nHit : {hit}")
    print(f"Page Faults : {page_fault}")
    


if __name__ == "__main__":
    page_references_string = [1, 3, 0, 3, 5, 6, 3]
    frames_count = 3
    fifo(page_references_string, frames_count)
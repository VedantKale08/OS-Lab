def fifo_replace(frames, page_number, page_table):
    if page_number in frames:
        return f"Page {page_number} already in memory. Page Hit"
    for i, frame in enumerate(frames):
        if frame is None:
            frames[i] = page_number
            page_table[page_number] = i
            return f"Page {page_number} inserted in frame {i}. Page Miss"
    removed_page = frames.pop(0)
    frames.append(page_number)
    removed_frame = page_table.pop(removed_page)
    page_table[page_number] = removed_frame
    return f"Page {page_number} inserted in frame {removed_frame}. Page {removed_page} replaced. Page Miss"





def paging_system(las_size, page_size, num_frames):
    num_pages = las_size // page_size
    frames = [None] * num_frames
    page_table = {}

    while True:
        page_input = input("Enter page number to transfer to main memory (Enter 'exit' to exit): ")
        if page_input.lower() == 'exit':
            break
        try:
            page_number = int(page_input)
            if page_number < 0 or page_number >= num_pages:
                print("Invalid page number. Please enter a number between 0 and", num_pages - 1)
                continue
            print(fifo_replace(frames, page_number, page_table))

            print("|\n  Frame number \t| Page number\t|")
            print("+---------------+---------------+")
            for frame in range(num_frames):
                if frame in page_table.values():
                    for page, f in page_table.items():
                        if f == frame:
                            print(f"|\t{frame} \t|\t {page} \t|")
                else:
                    print(f"|\t{frame} \t|\t NULL \t|")
            print("+---------------+---------------+")
            print("\n")

        except ValueError:
            print("Invalid input. Please enter a valid page number.")




las_size = int(input("Enter Logical Address Space size (Bytes): "))
pas_size = int(input("Enter Physical Address Space Size (Bytes): "))
page_size = int(input("Choose any page size: "))
num_frames = pas_size // page_size
print(f"The number of frames in primary memory are {num_frames}")

paging_system(las_size, page_size, num_frames)


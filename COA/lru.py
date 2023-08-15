def lru_page_replacement(pages, capacity):
    frames = []  
    page_faults = 0  
    hit =0
    for page in pages:
        print("Page:", page)
        if page in frames:
            
            frames.remove(page)
        elif len(frames) == capacity:
            
            frames.pop(0)
            page_faults += 1

        else:
            hit += 1
        frames.append(page)

        
        print("Frames: ", end="")
        for frame in frames:
            print(frame, end=" ")

    return page_faults,hit



page_list = [2,3,2,1,5,2,4,5,3,2,3,2]
frame_capacity = 4
faults,hit = lru_page_replacement(page_list, frame_capacity)
print("Hit ratio", hit*100/(hit+faults+2))
# print("Total page faults:", faults)

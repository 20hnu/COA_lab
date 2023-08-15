def fifo_page_replacement(pages, capacity):
    frames = []  
    page_faults = 0  
    hit=0    
    for page in pages:
        print("Page:", page)
        if page not in frames:
            
            if len(frames) == capacity:
                frames.pop(0)

            
            frames.append(page)
            print("!!!MISS!!!")
            page_faults += 1
        else:
            hit+=1
            print("!!!HIT!!!")
        # print(frames)
    return page_faults,hit


page_list = [2,3,2,1,5,2,4,5,3,2,3,2]
frame_capacity = 4
faults,hit = fifo_page_replacement(page_list, frame_capacity)
print("Hit ratio", hit*100/(hit+faults))
# successful attempt

with open("advent-of-code/2024/input/1.txt","r") as inp:

    list1, list2 = [], []
    answer = 0

    for line in inp:
        list1.append(int(line.strip().split("   ")[0]))
        list2.append(int(line.strip().split("   ")[1]))
    
    for nL in list1:
        count = 0
        for rL in list2:
            if nL == rL:
                count += 1
        answer += nL*count

    print(answer)
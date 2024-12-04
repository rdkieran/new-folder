# successful attempt 

with open("advent-of-code/2024/input/1.txt","r") as i:
    list1, list2 = [], []
    answer = 0

    for line in i:
        list1.append(int(line.strip().split("   ")[0]))
        list2.append(int(line.strip().split("   ")[1]))
    
    list1, list2 = sorted(list1), sorted(list2)
    
    for n in range(len(list1)):
        answer += abs(list1[n]-list2[n])

    print(answer)
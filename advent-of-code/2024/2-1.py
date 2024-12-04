def runCheck(report):
    if incrementCheck(report) == True:
        return riseFallCheck(report)
    else:
        return False

def incrementCheck(report):
    for i in range(len(report)):
        if i == len(report)-1:
            return True
        if abs(report[i]-report[i+1]) > 3:
            return False
        
def riseFallCheck(report):
    if report[0]-report[-1] < 0:
        report.reverse()
    for i in range(len(report)):
        if i == len(report)-1:
            return True
        if report[i] < report[i+1]:
            return False
        elif report[i] == report[i+1]:
            return False

def main():
    with open('advent-of-code/2024/input/2.txt','r') as inp:
        safeCount = 0
        for line in inp:
            report = []
            for level in line.strip().split(' '):
                report.append(int(level))
            if runCheck(report):
                print(report)
                safeCount += 1
    print(safeCount)
main()
import matplotlib

def importFile(filename):
    outList = []
    fil = open(filename)
    for line in fil:
        outList.append(line.strip())
    return outList

def insertionSort():
    importFile("testfiles/testcase0.txt")
    pass

def bubbleSort(list):
    bubbleList = list.copy()

    # x er mængden af gange løkken er blevet kørt igennem #
    x = 0

    # 
    for e in range(len(bubbleList) - 1):
        x = x + 1

        #
        for i in range(len(bubbleList) - x):

            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i], bubbleList[i+1] = bubbleList[i+1], bubbleList[i]
    return bubbleList

if __name__ == "__main__":
    insertionSort()

    L = [4, 3, 2, 1]
    print(bubbleSort(L))

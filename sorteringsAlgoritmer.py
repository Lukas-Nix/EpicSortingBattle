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

def bubbleSort():
    pass


if __name__ == "__main__":
    insertionSort()

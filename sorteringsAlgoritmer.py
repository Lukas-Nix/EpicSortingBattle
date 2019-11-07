def importFile(filename):
    outList = []
    fil = open(filename)
    for line in fil:
        outList.append(line.strip())
    return outList

#I vores insertionSort giver vi den en parameter "file", så at når vi kalder på funktionen, kræver den en parameter
def insertionSort(file):
    #Vi laver et for loop som kigger på elementerne mellem 0 og længden af elementer i listen "file"
    for i in range(1,len(file)):
        key=file[i]

def bubbleSort():
    pass


if __name__ == "__main__":
    insertionSort()

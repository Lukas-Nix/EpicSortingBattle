#I vores insertionSort giver vi den en parameter "list", så at når vi kalder på funktionen, kræver den en parameter
def insertionSort(list):
    #vi gemmer parameteren, list, som sin egen liste
    sejereListe = list
    #Vi laver et for loop som kigger på elementerne mellem 1, det andet element i listen, og mængden af elementer i listen "sejereListe"
    for i in range(1, len(sejereListe)):
        key = sejereListe[i]

        j = i - 1
        while j >= 0 and key < sejereListe[j]:
            sejereListe[j + 1] = sejereListe[j]
            j -= 1
        sejereListe[j + 1] = key
    return sejereListe


def bubbleSort():
    importFile("testfiles/testcase0.txt")
    pass


if __name__ == "__main__":
    joy=[22,5,1,7,2,7,98,3]
    insertionSort(joy)
    #print(sejereListe)
    for i in range(len(joy)):
        print("% d" % joy[i])

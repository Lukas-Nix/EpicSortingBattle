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

    # x er mængden af gange løkken er blevet kørt igennem. så her starter den ud med at havde været kørt igennem 0 gange#
    x = 0

    # her tager den lægnden af af elementer og når de er kørt kørt igennem er x + 1, altså lykken er kørt igennem 1 gang#
    for e in range(len(bubbleList) - 1):
        x = x + 1

        # her gør den så noget i lykken ved en bestemt betingelse #
        for i in range(len(bubbleList) - x):

            # Hvis et element er større end det næste element i listen, skifter de plads #
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i], bubbleList[i+1] = bubbleList[i+1], bubbleList[i]

    #listen bliver smidt ud ændret til at være sorteret #
    return bubbleList

if __name__ == "__main__":
    insertionSort()

    L = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubbleSort(L))

#I vores insertionSort giver vi den en parameter "list", så at når vi kalder på funktionen, kræver den en parameter
def insertionSort(list):
    #vi gemmer parameteren, list, som sin egen liste
    sejereListe = list
    #Vi laver et for loop som bliver kørt igennem et antal gange lig med størrelsen på listen "sejereListe"
    for i in range(0, len(sejereListe)):

        #Igennem hvert loop bliver der defineret "key" til at være det nye element som den er nået til i listen.
        key = sejereListe[i]

        #
        j = i - 1
        while j >= 0 and key < sejereListe[j]:
            sejereListe[j + 1] = sejereListe[j]
            j -= 1
        sejereListe[j + 1] = key
    return sejereListe


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
<<<<<<< HEAD
    insertionSort()

    L = [4, 3, 2, 1]
    print(bubbleSort(L))
=======
    joy=[22,5,1,7,2,7,98,3]
    insertionSort(joy)
    #print(sejereListe)
    for i in range(len(joy)):
        print("% d" % joy[i])
>>>>>>> 6f4336dfe3f89d483bd69de355e30eef0511c7b1

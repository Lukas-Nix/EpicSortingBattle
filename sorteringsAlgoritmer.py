#I vores insertionSort giver vi den en parameter "list", så at når vi kalder på funktionen, kræver den en parameter
def insertionSort(list):
    #vi gemmer parameteren, list, som sin egen liste, så vi ikke påvirker den originalle liste 
    sejereListe = list
    #Vi laver et for loop som bliver kørt igennem et antal gange lig med størrelsen på listen "sejereListe"
    for i in range(1, len(sejereListe)):
        #Igennem hvert loop bliver der defineret "key" til at være det nye element som den er nået til i listen.
        key = sejereListe[i]

        #Efter det gemmer den så elementet før det nuværende element som sit eget element
        j = i - 1

        '''
        I hvert loop har den så den nuværende element og elementet før det element der arbejdes på,
        ved at j er et tal mindre end i, altså et element før


        Nu skal koden begynde at sortere.
        I det følgende loop vil den tjekke om det originalle element er mindre end elementet før, og hvis det er, så bytter den plads på dem.
        '''
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
    L = [4, 3, 2, 1]
    print(bubbleSort(L))
    joy=[22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3]
    insertionSort(joy)
    #print(sejereListe)
    for i in range(len(joy)):
        print("% d" % joy[i])

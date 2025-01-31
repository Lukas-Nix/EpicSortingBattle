#I vores insertionSort giver vi den en parameter "list", så at når vi kalder på funktionen, kræver den en parameter
def insertionSort(list):
    #vi gemmer parameteren, list, som en kopi, så vi ikke påvirker den originale
    sejereListe = list.copy()
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
    #Så smider vi den tilbage som sejereListe
    return sejereListe

def bubbleSort(list):

    bubbleList = list.copy()

    # x er mængden af gange løkken er blevet kørt igennem. så her starter den ud med at havde været kørt igennem 0 gange#
    x = 0

    # her tager den lægnden af af elementer og når de er kørt kørt igennem er x + 1, altså lykken er kørt igennem 1 gang
    for e in range(len(bubbleList) - 1):
        x = x + 1

        # her gør den så noget i lykken ved en bestemt betingelse
        for i in range(len(bubbleList) - x):

            # Hvis et element er større end det næste element i listen, skifter de plads #
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i], bubbleList[i+1] = bubbleList[i+1], bubbleList[i]

    #listen bliver smidt ud ændret til at være sorteret
    return bubbleList

def selectionSort(list):
    #vi gemmer parameteren, list, som en kopi, så vi ikke påvirker den originale
    selection = list.copy()

    #Vi laver et for loop som kører igennem for hvert element i den nye liste
    for i in range(len(selection)):
        # Hver gang loopet går igennem, så gemmer vi det mindste tal som er det element vi er nået til et loopet
        mindsteTal = i

        '''
        Så kører vi igennem listen igen og tjekker om det nye tal er mindre end mindsteTal.
        Hvis den er, så definerer vi det mindsteTal til at være det mindre tal
        '''
        for j in range(i+1,len(selection)):
            if selection[mindsteTal]>selection[j]:
                mindsteTal=j

        # til sidst bytter vi om på det element vi er nået til i vores første for loop, med det mindste tal af elementerne i talene efter
        selection[i], selection[mindsteTal] = selection[mindsteTal], selection[i]

    #så smider vi den tilbage til brugeren
    return selection

def mergeSort():
    pass

if __name__ == "__main__":

    L = [4, 3, 2, 1]
    L2 = [4, 3, 2, 6,1,8,7]
    print(bubbleSort(L))
    joy=[22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3,22,5,1,7,2,7,98,3]
    print(insertionSort(joy))
    print(selectionSort(L2))

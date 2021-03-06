def Merge(first, second):
    
    a = 0
    b = 0
    mergedArray = []

    while a < len(first) and b < len(second):
        if first[a] < second[b]:
            mergedArray.append(first[a])
            a = a + 1
        elif first[a] > second[b]:
            mergedArray.append(second[b])
            b = b + 1
        else:
            mergedArray.append(first[a])
            mergedArray.append(second[b])
            a = a + 1
            b = b + 1

    while a < len(first):
        mergedArray.append(first[a])
        a = a + 1

    while b < len(second):
        mergedArray.append(second[b])
        b = b + 1

    return mergedArray  


# The Strand Sort Function
def StrandSort(inputArray):
    # outputArray for accumulating results
    outputArray = []
    # run while loop while inputArray is not empty
    while len(inputArray) > 0:
        # clear the sublist and 
        # remove the first element from the 
        # input array and put in the sublist
        sublist = [ inputArray.pop(0) ]
        # loop over the inputArray
        x = 0
        while x < len(inputArray):
            # check if the current value in the inputArray is greater than the sublist
            # if it is, remove that element from the inputArray and put it at the end
            # of the sublist
            if inputArray[x] > sublist[-1]:
                sublist.append(inputArray.pop(x))
            # increment x to keep the while loop moving forward
            else:
                x = x + 1
        # merge sublist with outputArray and store the results in outputArray
        outputArray = Merge(sublist, outputArray)
    return outputArray

def strandsort(unsorted):
    items = len(unsorted)
    sortedBins = []
    while( len(unsorted) > 0 ):
        highest = float("-inf")
        newBin = []
        i = 0
        while( i < len(unsorted) ):
            if( unsorted[i] >= highest ):
                highest = unsorted.pop(i)
                newBin.append( highest )
            else:
                i=i+1
        sortedBins.append(newBin)
    sorted = []
    while( len(sorted) < items ):
        lowBin = 0
        for j in range( 0, len(sortedBins) ):
            if( sortedBins[j][0] < sortedBins[lowBin][0] ):
                lowBin = j
        sorted.append( sortedBins[lowBin].pop(0) )
        if( len(sortedBins[lowBin]) == 0 ):
            del sortedBins[lowBin]
    return sorted

arr = [10, 6, 8, 8, 3, 2, 7, 4,8, 8, 3, 2, 7, 4, 6, 8, 8, 3, 2, 7, 4,9, 11, 10, 9, 6, 10, 3, 5, 8, 8, 3, 2, 7, 4,8, 8, 3, 2, 7, 4, 6, 8, 8, 3, 2, 7, 4,9, 11, 10, 9, 6, 8, 8, 3, 5, 5, 7, 8, 15, 49, 65, 2]

print strandsort(arr)


def selectAStrings(array):
    newArray = []

    for i in range(len(array)):
        if array[i].startswith('a'): # O(1) p/cada
            newArray.append(array[i]) # O(1) p/cada

    return  newArray

#Por causa do for a complexidade de tempo é de O(n)

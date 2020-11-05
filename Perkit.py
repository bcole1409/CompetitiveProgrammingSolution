import itertools

def findCombos(ingredients):
    #create list to store all combos, this will be what this function returns to main
    allCombinations = []
    for i in range(len(ingredients)+1):
        combos = itertools.combinations(ingredients,i)
        combolist = list(combos)
        allCombinations += combolist
    return(allCombinations)

def main():
    #number of ingredients
    n = int(input())

    #generate list of ingredients
    ingredients = [""]*n
    
    #populate ingredients array
    for i in range(n):
        ingredients[i] = str(input())

    #Calls seperate function ("find Combos") to receive all combinations from our given inputs
    allCombos = findCombos(ingredients)

    #this variable will contain the answer, which is the minimal difference
    minimumDifference = 1000000000

    #STRING SPLIT to help us organize S and B
    StringSplit = ""

    #iterate though all combos
    for item in range(0,len(allCombos)):
        #if item is zero, there are no ingredients stored, so ignore
        if item == 0:
            continue
        else:
            #intialize S and B
            Sourness = 1
            Bitterness = 0

            #Calculates S and B for given combinations
            for combos in allCombos[item]:
                #split string by space into two seperate variables
                StringSplit = combos.split(" ")
                Sourness *= int(StringSplit[0])
                Bitterness += int(StringSplit[1])

            #calculate the absolute value between S and B totals 
            if(abs(Sourness - Bitterness) < minimumDifference):
                minimumDifference = abs(Sourness - Bitterness)

    #prints result of smallest difference
    print(int(minimumDifference))

#main
if __name__ == "__main__":         
    main()




def main():
    global CountRecursion
    CountRecursion = 0
    #gather input from first input line
    #N = NUMBER OF INGREDIENTS
    #M - NUMBER OF MISMATCHES
    N, M = map(int, input().split())

    #create list of mismatches
    #INITIALIZE ARRAY
    missArray = [[None]*N]*M
    
    for i in range(M):
        in1,in2 = map(int, input().split())
        missArray[i] = [in1,in2]

    #general array of ingredients
    arrayOfIngredients = []
    for i in range(N):
        arrayOfIngredients.append(i+1)

    all_subsets(arrayOfIngredients,missArray)
    
    print(CountRecursion)
    
def createSubset(subset,notAllowed):
    global CountRecursion
    Counter = 0
    for item in notAllowed:
        #reset counter if not invalid
        Counter = 0
        
        for ingredient in item:
            if ingredient in subset:
                Counter += 1
                if Counter == 2:
                    return
                
    CountRecursion += 1     
    
def all_subsets(givenArray,missArray):
    subset = [[0]]*len(givenArray)
    lists = [[]]
    helper(givenArray,subset,0,missArray)

def helper(givenArray,subset,i,prohibited):
    #finished creating subsets
    if i == len(givenArray):
        createSubset(subset,prohibited)
        return
    
    else:
        subset[i] = None
        helper(givenArray,subset,i+1,prohibited)
        subset[i] = givenArray[i]
        helper(givenArray,subset,i+1,prohibited)

if __name__ == "__main__":
    main()

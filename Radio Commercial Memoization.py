#globals
#Number of commercial breaks. #Price of Commercial Break
N,P = map(int, input().split())

#memoization
result = [0]*N

#STUDENT lISTENERS
Students =  list(map(lambda N: int(N) - P, input().split()))

def computeMaxSubArray(index):
    if index == 0:
        result[index] = Students[0]
        return result[index]
    else:
        result[index] = Students[index] + max(0, computeMaxSubArray(index-1))
        return result[index] 
     
def main():
    for i in range(len(Students)):
        computeMaxSubArray(i)  
    print(max(result))


if __name__ == "__main__":
    main()

def main():
    #gather input from user
    T = int(input())
    
    for num in range(T):
        N = int(input())
        #initialize array
        weight = []
        
        for i in range(N):
            #add to array
            #W = input().split()
            W = list(map(int, input().split()))
            weight.append(W[0] * sum(W[1:])/len(W[1:]))
            #weight.append(input().split())
        weight.sort()
        for i in range(1, len(weight)):
            weight[i] = weight[i - 1] + weight[i]
        print(sum(weight)/(N))

if __name__ == "__main__":
    main()

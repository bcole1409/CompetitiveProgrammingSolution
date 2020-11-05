def main():
    #map data given user/computer input
    N,K = map(int, input().split())

    #initialize array
    fib = [0,1,1]

    #create array of fib numbers
    for i in range(N+1):
        fib.append(fib[-1] + fib[-2])
    
    #do until N is 2 so we can narrow down between two letters
    while N > 2:
        #if k is greater than, fib n -2
            #reduce K by fib(n-2)
            #reduce N by 1
        if K > fib[N-2]:
            K -= fib[N-2]
            N -= 1
        else:
            #other wise reduce N by -2
            N -= 2

    #once we get N down to 2 or less, we can determine what letter is in the Kth spot
    if N == 1:
        print ("N")
    if N == 2:
        print ("A")

if __name__=="__main__":
    main()

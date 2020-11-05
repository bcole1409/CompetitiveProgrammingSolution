def walrus(DP,N,Target):
    for i in range(1,N):
        for j in range(1,N):
            if j > i:
                Temp1 = abs(Target - DP[i][j-1])
                Temp2 = abs(Target - DP[i-1][j])
                Temp3 = abs(Target - (DP[i][0] + DP[0][j]))
                Temp4 = abs(Target - (DP[i][j-1] + DP[0][j]))

                if Temp1 < Temp2 and Temp1 < Temp3 and Temp1 < Temp4:
                    DP[i][j] = DP[i][j-1]
                elif Temp2 < Temp1 and Temp2 < Temp3 and Temp2 < Temp4:
                    DP[i][j] = DP[i-1][j]
                elif Temp3 < Temp1 and Temp3 < Temp2 and Temp3 < Temp4:
                    DP[i][j] = DP[i][0] + DP[0][j]
                else:
                    DP[i][j] = DP[i][j-1] + DP[0][j]
            else:
                if Target - DP[i-1][j] < Target - DP[i][j-1]:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = DP[i][j-1]

    return DP[i][j]

def main():
    #gather input from user
    N = int(input())

    #INITIALIZE WEIGHT LIST
    Weights = [None]
    for i in range(N):
        Weights.append(int(input()))
                       
    #initialize DP array and first column
    DP = [[0 for i in range(0,N+1)] for j in range(0,N+1)]
    for i,j in enumerate(Weights):
        DP[i][0] = j
        DP[0][i] = j

    #Length of DP is needed for WALRUS
    Length = len(DP)

    #Target = 1000 specified in problem
    T = 1000

    print(walrus(DP,Length,T))

if __name__ == "__main__":
    main()

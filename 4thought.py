##################################################################################################################################################################################
###Question
#Write a program which, given an integer n as input, will produce a mathematical expression whose solution is n. The solution is restricted to using exactly four 4’s and exactly three of the binary operations selected from the set {∗,+,−,/}. The number 4 is the ONLY number you can use. You are not allowed to concatenate fours to generate other numbers, such as 44 or 444.

#For example given n=0, a solution is 4∗4−4∗4=0. Given n=7, a solution is 4+4−4 / 4=7. Division is considered truncating integer division, so that 1/4 is 0 (instead of 0.25). Assume the usual precedence of operations so that 4+4∗4=20, not 32. Not all integer inputs have solutions using four 4’s with the aforementioned restrictions (consider n=11).

#Hint: Using your forehead and some forethought should make an answer forthcoming. When in doubt use the fourth.

##Input
#Input begins with an integer 1≤m≤1000, indicating the number of test cases that follow. Each of the next m lines contain exactly one integer value for n in the range −1000000≤n≤1000000.

##Output
#For each test case print one line of output containing either an equation using four 4’s to reach the target number or the phrase no solution. Print the equation following the format of the sample output; use spaces to separate the numbers and symbols printed. If there is more than one such equation which evaluates to the target integer, print any one of them.
##################################################################################################################################################################################

m = int(input())
ops= ['+', '-', '*', '//']
for i in range(m):

    #input number
    n = int(input())

    #initialize res which will tell us if we found 4's in nested loop so we can stop iterating
    res = 0
    
    #Base Case so we don't have to iterate for no reason
    if n > 256 or n < -60:
        res = 1
        print("no solution")

    #if result = 0, then we know it fits criteria mentioned above
    if res == 0:
        for op1 in ops:
            if res == 1:
                    break
            for op2 in ops:
                if res == 1:
                    break
                for op3 in ops:
                    expr = f'4 {op1} 4 {op2} 4 {op3} 4'
                    if eval(expr) == n:
                        #correct format: need to replace "//" with "/"
                        if op1 == '//':
                            op1 = '/'
                        if op2 == '//':
                            op2 = '/'
                        if op3 == '//':
                            op3 = '/'
                            
                        #generate new expression with correct format
                        expr = f'4 {op1} 4 {op2} 4 {op3} 4'
                        
                        #set res to 1 so we know to break nested-loop
                        res = 1
                        print(f'{expr} = {n}')
                        break

    #if we found no solution in loop, res will tell us so...
    if res == 0:          
        print('no solution')




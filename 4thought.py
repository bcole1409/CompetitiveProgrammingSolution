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




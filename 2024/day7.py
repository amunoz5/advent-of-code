with open("data/day7.txt") as file:
    data = [l.strip().split(':') for l in file]

data = [[int(x[0]), list(map(int,(x[1].strip().split())))] for x in data]

#print(data)
#[test_val, [operators, ...]]

#determine which test values could possibly be produced by placing any combination of operators into their calibration equations

#always evaluated left-to-right

def evaluate(operation, result):
    val1=operation[0]
    val2=0
    res=0
    
    for i in range(len(operation)):
        elem = operation[i]
        if elem in operators:
            val2 = operation[i+1]
            if elem=='+':
                res = val1+val2
            elif elem=='*':
                res = val1*val2
            elif elem=='||':
                res = val1*10**(len(str(val2)))+val2
            else:
                print("[evaluate] unsupported operator in operation", operation)
            val1 = res
    #print(operation,"=",res,'->', res==result)
    return res == result

#operators: +, *
operators = ['+', '*', '||']
def permute_eval(eq, i=0, current_eq=[]):
    #print("[permute_eval]", eq, i, current_eq)
    if i >= len(eq):
        return [current_eq]

    combinations = []

    if eq[i]!= 'op':
        combinations.extend(permute_eval(eq, i+1, current_eq+[eq[i]]))
    else:
        #iterate over operators
        for op in operators:
            combinations.extend(permute_eval(eq, i+1, current_eq+[op]))
    #print(combinations)
    return combinations

star_1=0
for line in data:
    expected_res = line[0]
    equation = line[1]
    
    #insert operands to equation
    eq_w_wildcards = []
    for e in equation:
        eq_w_wildcards+=[e,'op']
    eq_w_wildcards = eq_w_wildcards[:-1]
    eq_w_operands = permute_eval(eq_w_wildcards)

    #print(equation, eq_w_operands)
    #check operations
    num_valid_combo=0
    for eq in eq_w_operands:
        num_valid_combo+= 1 if evaluate(eq, expected_res) else 0

    #print(num_valid_combo, line)
    star_1+=expected_res if num_valid_combo>0 else 0

#total calibration result, which is the sum of the test values(expected_res) from just the equations that could possibly be true

print("star 1:", star_1)
#print("star 2:", star_2)

#print("-- tests --")
#evaluate([10,'+',19],190)
#evaluate([10,'*',19],190)
#evaluate([15,'||',6],156)
#evaluate([10,'||',19],1019)
#evaluate([81,'+',40,'*',27],3267)
#evaluate([81,'*',40,'+',27],3267)
#permute_eval([81,'op',40,'op',27])

# time for star 1 -> 22.40 min
# time for star 2 -> 5.29 min 
# time for day 7 -> 28.09  min

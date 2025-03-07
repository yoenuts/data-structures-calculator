import sys
import math
import re

def replace_fact(match):
    x = int(match.group(1))
    return f'math.factorial({x})'
    

try:
    #Initializes mainNum
    mainNum = sys.argv[1]
    # mainNum = "5+67+8!+5!,1,3,1"
    variables = mainNum.split(',')  # Split the input string using the comma delimiter
    sum = 0
    prod = 1
    func = variables[0]
    tempA = int(variables[1])
    tempB = int(variables[2])
    type = int(variables[3])
    
    #EDGE CASES
    fact = r'(\d+)!'
    func = func.replace("^", "**")
    func = re.sub(fact, replace_fact, func)
    

    
    if len(variables) != 4:
        raise ValueError("Expected 4 variables")

    for i in range(tempA, tempB+1):
        if(type == 1):
            sum += eval(func)
        elif(type == 2):
            prod *= eval(func)
        
    if(type == 1):print(sum)
    elif(type == 2):print(prod)


except Exception as e:
    print(f"Err", e)
    sys.exit(1)
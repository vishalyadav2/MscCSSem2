#Write a program to illustrate the generation on OPM for the input operator Grammar.
def generate_opm(grammar):
    operators = []
    precedence = {}
    
    # Step 1: Extract operators and precedence relations from the grammar
    for rule in grammar:
        op = rule.split()[1]  # Assuming grammar is in the form 'E + E', 'E * E', etc.
        if op not in operators:
            operators.append(op)
            precedence[op] = {}
        
        # Extract precedence relation (relation symbol and direction)
        prec = rule.split()[2]
        direction = rule.split()[3]
        
        # Store precedence relation in the dictionary
        precedence[op][prec] = direction
    
    # Step 2: Generate the Operator Precedence Matrix (OPM)
    opm = [[None] * (len(operators) + 1) for _ in range(len(operators) + 1)]
    
    # Fill the top row and first column of the OPM with operators
    opm[0][0] = ''
    for i in range(1, len(operators) + 1):
        opm[0][i] = operators[i - 1]
        opm[i][0] = operators[i - 1]
    
    # Fill the OPM based on the precedence relations
    for i in range(1, len(operators) + 1):
        for j in range(1, len(operators) + 1):
            op1 = opm[i][0]
            op2 = opm[0][j]
            if op1 in precedence and op2 in precedence[op1]:
                opm[i][j] = precedence[op1][op2]
    
    return opm

# Example grammar
grammar = [
    "E + E >",
    "E - E >",
    "E * E >>",
    "E / E >>",
    "E ^ E <<",
    "( E ) ="
]

# Generate and print the Operator Precedence Matrix (OPM)
opm = generate_opm(grammar)

# Print the OPM in a readable format
print("Operator Precedence Matrix:")
for row in opm:
    print(row)

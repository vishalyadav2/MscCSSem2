#Write a C/C++/JAVA/Python code to demonstrate the step-by-step parsing of input string to an OPG using already provided OPM
def parse_expression(expression, opm):
    # Convert the expression into a list of tokens (operands and operators)
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    # Add end marker to tokens to indicate end of input
    tokens.append('$')
    # Operator stack and operand stack
    operator_stack = []
    operand_stack = []
    
    # Precedence lookup function
    def precedence(op):
        if op in opm:
            return opm[op]
        else:
            return -1
    
    # Parsing function
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.isdigit():  # Operand case
            operand_stack.append(token)
            i += 1
        elif token in opm:  # Operator case
            while operator_stack and precedence(operator_stack[-1]) >= precedence(token):
                op = operator_stack.pop()
                if op != '(':
                    right = operand_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(f"{left} {op} {right}")
            operator_stack.append(token)
            i += 1
        elif token == '(':  # Left parenthesis
            operator_stack.append(token)
            i += 1
        elif token == ')':  # Right parenthesis
            while operator_stack[-1] != '(':
                op = operator_stack.pop()
                if op != '(':
                    right = operand_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(f"{left} {op} {right}")
            operator_stack.pop()  # Remove '('
            i += 1
        elif token == '$' and len(operator_stack) > 0:  # End marker
            while len(operator_stack) > 0:
                op = operator_stack.pop()
                if op != '(':
                    right = operand_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(f"{left} {op} {right}")
            i += 1
    
    # Final expression will be the only element in operand_stack
    return operand_stack[0]

# Example Operator Precedence Matrix (OPM)
opm = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '(': 0,
}

# Example expression
expression = "2 + 3 * 4 - 1"

# Parse the expression using the provided OPM
parsed_expression = parse_expression(expression, opm)

# Print the parsed expression
print("Parsed Expression:", parsed_expression)

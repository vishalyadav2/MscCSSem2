#Write a code to generate the DAG for the input arithmetic expression

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

class DAG:
    def __init__(self):
        self.nodes = {}
    
    def get_node(self, value):
        # Avoid duplicate nodes for the same value
        if value in self.nodes:
            return self.nodes[value]
        else:
            node = Node(value)
            self.nodes[value] = node
            return node

    def add_operation(self, operator, left_operand, right_operand=None):
        # Create unique node keys for subexpressions to avoid duplicates
        if right_operand:
            key = f"({left_operand.value} {operator} {right_operand.value})"
        else:
            key = f"({operator}{left_operand.value})"

        if key in self.nodes:
            return self.nodes[key]
        
        node = Node(operator)
        node.left = left_operand
        node.right = right_operand
        self.nodes[key] = node
        return node

    def display(self):
        # Simple print to display the nodes and their connections
        print("DAG Nodes and Connections:")
        for key, node in self.nodes.items():
            left = node.left.value if node.left else None
            right = node.right.value if node.right else None
            print(f"Node {node.value}: Left -> {left}, Right -> {right}")

def parse_expression_to_dag(expression, dag):
    # Stack to store operators and operands
    operators = []
    operands = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Process numbers (operands)
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            operand = dag.get_node(expression[i:j])
            operands.append(operand)
            i = j - 1
        elif expression[i] in "+-*/":
            # Process operators
            while (operators and operators[-1] in "+-*/" and
                   precedence(operators[-1]) >= precedence(expression[i])):
                process_operator(operators, operands, dag)
            operators.append(expression[i])
        i += 1

    while operators:
        process_operator(operators, operands, dag)

    return operands[-1] if operands else None

def precedence(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0

def process_operator(operators, operands, dag):
    op = operators.pop()
    right = operands.pop()
    left = operands.pop()
    operands.append(dag.add_operation(op, left, right))

# Example usage
expression = "3+4*5-6"
dag = DAG()
root = parse_expression_to_dag(expression, dag)

# Display the DAG structure
dag.display()


#Write a program to illustrate the generation on SPM for the input grammar
class Grammar:
    def __init__(self, non_terminals, terminals, start_symbol, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions

def compute_first(symbol, productions, first_sets):
    if symbol not in first_sets:
        first_sets[symbol] = set()
    
    if symbol in grammar.terminals:
        first_sets[symbol].add(symbol)
        return first_sets[symbol]

    for production in productions:
        if production[0] == symbol:
            rhs = production[1]
            if rhs == '':
                first_sets[symbol].add('')
            else:
                for sym in rhs:
                    first_sets[symbol].update(compute_first(sym, productions, first_sets))
                    if '' not in first_sets[sym]:
                        break
    return first_sets[symbol]

def compute_follow(symbol, productions, follow_sets, first_sets, start_symbol):
    if symbol not in follow_sets:
        follow_sets[symbol] = set()
    if symbol == start_symbol:
        follow_sets[symbol].add('$')  # End of input marker

    for production in productions:
        lhs, rhs = production
        for i, sym in enumerate(rhs):
            if sym == symbol:
                if i + 1 < len(rhs):
                    next_sym = rhs[i + 1]
                    follow_sets[symbol].update(first_sets[next_sym] - {''})
                    if '' in first_sets[next_sym]:
                        follow_sets[symbol].update(compute_follow(lhs, productions, follow_sets, first_sets, start_symbol))
                else:
                    follow_sets[symbol].update(compute_follow(lhs, productions, follow_sets, first_sets, start_symbol))

    return follow_sets[symbol]

def generate_spm(grammar):
    first_sets = {}
    follow_sets = {}

    for non_terminal in grammar.non_terminals:
        compute_first(non_terminal, grammar.productions, first_sets)

    for non_terminal in grammar.non_terminals:
        compute_follow(non_terminal, grammar.productions, follow_sets, first_sets, grammar.start_symbol)

    spm = {}
    symbols = list(grammar.non_terminals) + list(grammar.terminals) + ['$']

    for sym1 in symbols:
        spm[sym1] = {}
        for sym2 in symbols:
            spm[sym1][sym2] = ' '

    for lhs, rhs in grammar.productions:
        for i in range(len(rhs) - 1):
            if rhs[i] in grammar.terminals and rhs[i+1] in grammar.terminals:
                spm[rhs[i]][rhs[i+1]] = '='
            if rhs[i] in grammar.terminals and rhs[i+1] in grammar.non_terminals:
                for sym in first_sets[rhs[i+1]]:
                    if sym:
                        spm[rhs[i]][sym] = '<'
            if rhs[i] in grammar.non_terminals and rhs[i+1] in grammar.terminals:
                for sym in follow_sets[rhs[i]]:
                    if sym:
                        spm[sym][rhs[i+1]] = '>'

    return spm

# Example Grammar
non_terminals = {'S', 'A'}
terminals = {'a', 'b'}
start_symbol = 'S'
productions = [
    ('S', 'aA'),
    ('A', 'b'),
    ('A', '')
]
grammar = Grammar(non_terminals, terminals, start_symbol, productions)

# Generate the Simple Precedence Matrix
spm = generate_spm(grammar)

# Print the SPM
print("Simple Precedence Matrix:")
symbols = list(non_terminals) + list(terminals) + ['$']
print("  ", " ".join(symbols))
for sym1 in symbols:
    row = [sym1]
    for sym2 in symbols:
        row.append(spm[sym1][sym2])
    print(" ".join(row))

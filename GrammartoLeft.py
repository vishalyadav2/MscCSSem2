#Write a program to convert the given Right Linear Grammar to Left Linear Grammar form
class Grammar:
    def __init__(self, non_terminals, terminals, start_symbol, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions

    @staticmethod
    def reverse_production(production):
        """
        Reverses the right-hand side of a production.
        For example, A -> aB becomes A -> Ba
        """
        lhs, rhs = production
        reversed_rhs = ''.join(reversed(rhs))
        return lhs, reversed_rhs

    @staticmethod
    def convert_rlg_to_llg(rlg):
        """
        Converts a Right Linear Grammar (RLG) to a Left Linear Grammar (LLG).
        """
        llg_productions = []

        for production in rlg.productions:
            lhs, rhs = production

            # Reverse each production's right-hand side
            new_rhs = ''.join(reversed(rhs))

            # If the new right-hand side starts with a terminal followed by a non-terminal, swap them
            if len(new_rhs) == 2 and new_rhs[0] in rlg.terminals and new_rhs[1] in rlg.non_terminals:
                new_rhs = new_rhs[1] + new_rhs[0]

            llg_productions.append((lhs, new_rhs))

        return Grammar(rlg.non_terminals, rlg.terminals, rlg.start_symbol, llg_productions)

# Example Right Linear Grammar
rlg = Grammar(
    non_terminals={'S', 'A'},
    terminals={'a', 'b'},
    start_symbol='S',
    productions=[
        ('S', 'aS'),
        ('S', 'bA'),
        ('S', 'a'),
        ('A', 'aA'),
        ('A', 'b')
    ]
)

# Convert RLG to LLG
llg = Grammar.convert_rlg_to_llg(rlg)

# Print LLG details
print("LLG Non-terminals:", llg.non_terminals)
print("LLG Terminals:", llg.terminals)
print("LLG Start Symbol:", llg.start_symbol)
print("LLG Productions:")
for production in llg.productions:
    print(f"{production[0]} -> {production[1]}")


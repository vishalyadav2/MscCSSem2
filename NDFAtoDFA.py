#Write a program to convert the given NDFA to DFA.
class NDFA:
    def __init__(self, states, alphabet, start_state, accept_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

class DFA:
    def __init__(self, states, alphabet, start_state, accept_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

def ndfa_to_dfa(ndfa):
    # Start state of DFA is the epsilon closure of NDFA's start state
    start_state = frozenset(epsilon_closure(ndfa, {ndfa.start_state}))

    # Initialize DFA states and transitions
    dfa_states, unprocessed_states = {start_state}, [start_state]
    dfa_transitions, dfa_accept_states = {}, set()

    while unprocessed_states:
        current_state = unprocessed_states.pop()
        dfa_transitions[current_state] = {}

        # If any NDFA state in the current DFA state is an accept state, mark it
        if any(state in ndfa.accept_states for state in current_state):
            dfa_accept_states.add(current_state)

        for symbol in ndfa.alphabet:
            # Determine the next state for the current symbol
            next_state = frozenset(epsilon_closure(ndfa, move(ndfa, current_state, symbol)))
            dfa_transitions[current_state][symbol] = next_state

            # If the next state is new, add it to the set of DFA states
            if next_state not in dfa_states:
                dfa_states.add(next_state)
                unprocessed_states.append(next_state)

    return DFA(dfa_states, ndfa.alphabet, start_state, dfa_accept_states, dfa_transitions)

def epsilon_closure(ndfa, states):
    closure, stack = set(states), list(states)
    while stack:
        state = stack.pop()
        if (state, '') in ndfa.transitions:
            for next_state in ndfa.transitions[(state, '')]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    return closure

def move(ndfa, states, symbol):
    next_states = set()
    for state in states:
        next_states.update(ndfa.transitions.get((state, symbol), []))
    return next_states

# Example NDFA definition
ndfa = NDFA(
    {'q0', 'q1', 'q2'},  # States
    {'a', 'b'},          # Alphabet
    'q0',                # Start state
    {'q2'},              # Accept states
    {                    # Transitions
        ('q0', 'a'): {'q0', 'q1'},
        ('q0', ''): {'q1'},
        ('q1', 'b'): {'q2'},
        ('q2', 'a'): {'q2'}
    }
)

# Convert the NDFA to DFA
dfa = ndfa_to_dfa(ndfa)

# Print DFA details
print("DFA States:", dfa.states)
print("DFA Alphabet:", dfa.alphabet)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)
print("DFA Transitions:", dfa.transitions)


# Example NDFA definition
ndfa = NDFA(
    {'q0', 'q1', 'q2'},  # States
    {'a', 'b'},  # Alphabet
    'q0',  # Start state
    {'q2'},  # Accept states
    {  # Transitions
        ('q0', 'a'): {'q0', 'q1'},
        ('q0', ''): {'q1'},
        ('q1', 'b'): {'q2'},
        ('q2', 'a'): {'q2'}
    }
)

# Convert the NDFA to DFA
dfa = ndfa_to_dfa(ndfa)

# Print DFA details
print("DFA States:", dfa.states)
print("DFA Alphabet:", dfa.alphabet)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)
print("DFA Transitions:", dfa.transitions)

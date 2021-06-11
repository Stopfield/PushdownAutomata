from load_automata import components, functions

class Stack:

    def __init__ (self):
        self.stack = []

    def add(element):
        self.stack.append(element)

    def remove(self):
        self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

class PushDownAutomata:

    def __init__ (self, alphabet, states, stack_alphabet): # transition_function
        # Defines the symbols the automata can recognize
        self.sigma = alphabet # {a, b}

        # Defines the states, and their atributes
        self.states = states # {q0, ..., qf}
        self.start = self.define_start_state(elements)
        self.final = self.define_final_state(elements)
        self.current_state = self.start

        # Defines the stack atributes
        self.stack = Stack()
        self.V = stack_alphabet
        self.V = list(self.V)
        self.V.append(None)
        self.V = tuple(self.V)

        # Defines the transition funcion that defines the automata
        self.delta = self.populate_transition_method()

    def define_start_state(self, elements):
        return elements[3]
    
    def define_final_state(self, elements):
        return elements[4]

    def populate_transition_method(self):
        
        """
        Populate the delta atribute as a dictionary of dictionarys,
        simulation the behavior of a automata ((state, word) = (state'))
        """

        # transition_dict = {state : {element : {stack_el : 'Reject' for stack_el in self.V} for element in self.sigma} for state in self.states}

        transition_dict = {state : {element : 'Reject' for element in self.sigma} for state in self.states}

        for (state, dict_value) in transition_dict.items():
            print(f'Enter transitions for state {state}. If required, use "Reject"')

            for input_alphabet, transition_state in dict_value.items():
                transition_dict[state][input_alphabet] = input()

        print('\n Transiction Function Q x Sigma -> Q')
        print('Current State\tInput Alphabet\tNext State')
        for key, dict_value, teste in transition_dict.items():
            print(f'{key}\t\t{input_alphabet}\t\t{transition_state}')

digital_file = open('file.txt', 'r').read().splitlines()
elements = components(digital_file)
transition_function = functions(digital_file)

# print(elements)
print(transition_function)

automato = PushDownAutomata(elements[0], elements[1], elements[5])
# print(automato.sigma)
# print(automato.start)
# print(automato.final)
# print(automato.current_state)
# print(automato.states)
# print(automato.V)
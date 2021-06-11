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

    def __init__ (self, states, alphabet, transition_function, stack_alphabet):
        # Defines the symbols the automata can recognize
        self.sigma = alphabet # {a, b}

        # Defines the states, and their atributes
        self.states = states # {q0, ..., qf}
        self.start = self.define_start_state()
        self.final = self.define_final_state()
        self.current_state = self.start

        # Defines the transition funcion that defines the automata
        self.delta = self.populate_transition_function()

        # Defines the stack atributes
        self.stack = Stack()
        self.V = stack_alphabet

    def populate_transition_function(self):
        
        """
        Populate the delta atribute as a dictionary of dictionarys,
        simulation the behavior of a automata ((state, word) = (state'))
        """

        transition_dict = {state : {element : 'Reject' for element in self.sigma} for state in self.states}

        for state, dict_value in transiction_dict.items():
            print(f'Enter transitions for state {state}. If required, use "Reject"')

            for input_alphabet, transition_state in dict_value.items():
                transition_dict[key][input_alphabet] = input(f'Current State: {key}\tInput Alphabet: {input_alphabet}\tNext State : ')

        print('\n Transiction Function Q x Sigma -> Q')
        print('Current State\tInput Alphabet\tNext State')
        for key, dict_value in transiction_dict.items():
            print(f'{key}\t\t{input_alphabet}\t\t{transition_state}')
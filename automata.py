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
        self.sigma = list(self.sigma)
        self.sigma.append(None)
        self.sigma = tuple(self.sigma)

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
        self.delta = self.populate_transition_method(transition_function)

    def define_start_state(self, elements):
        return elements[3]
    
    def define_final_state(self, elements):
        return elements[4]

    def populate_transition_method(self, transition_function):
        
        """
        Populate the delta atribute as a dictionary of dictionarys,
        simulation the behavior of a automata ((state, word) = (state'))
        """

        transition_dict = {state : {element : {stack_el : 'Reject' for stack_el in self.V} for element in self.sigma} for state in self.states}

        for state, dict_value in transition_dict.items():

            for input_alphabet, stack_values in dict_value.items():

                for stack_simbol, transition_state in stack_values.items():

                    for transition in transition_function:
                        condition = transition[0] == state and transition[1] == input_alphabet and transition[2] == stack_simbol
                        if condition:
                            transition_dict[state][input_alphabet][stack_simbol] = transition[3]

        print(f"State\tSimbol\tStack\tNextState")
        for state, dict_value in transition_dict.items():

            for input_alphabet, stack_values in dict_value.items():

                for stack_simbol, transition_state in stack_values.items():

                    print("{}\t{}\t{}\t{}".format(state, input_alphabet, stack_simbol, transition_state))

        return transition_dict

    # def process_word(self, word):
        

digital_file = open('file.txt', 'r').read().splitlines()
elements = components(digital_file)
transition_function = functions(digital_file)

# print(elements)
# print(transition_function)
transition_function = list(transition_function)
transition_function[4] = list(transition_function[4])
transition_function[4][1] = None
transition_function[4][2] = None
transition_function[4] = tuple(transition_function[4])
transition_function = tuple(transition_function)
# print(transition_function[0])
# print(transition_function[1])
# print(transition_function[2])
# print(transition_function[3])
# print(transition_function[4])


automato = PushDownAutomata(elements[0], elements[1], elements[5])
# print(automato.delta)
# print(automato.sigma)
# print(automato.start)
# print(automato.final)
# print(automato.current_state)
# print(automato.states)
# print(automato.V)
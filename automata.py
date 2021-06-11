from load_automata import *

# print(components()[0])

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

    def __init__ (self, states = components()[1], alphabet = components()[0]):
        # Defines the symbols the automata can recognize
        self.sigma = alphabet

        # Defines the states, and their atributes
        self.states = states
        # self.start = self.define_start_state()
        # self.final = self.define_final_state()
        # self.current_state = self.start

        # # Defines the transition funcion that defines the automata
        # self.delta = transition_function

        # # Defines the stack atributes
        # self.stack = Stack()
        # self.V = stack_alphabet

print(PushDownAutomata().sigma)
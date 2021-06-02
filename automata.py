class PushDownAutomata:

    def __init__ (self, states, alphabet, transition_function):
        # Defines the symbols the automata can recognize
        self.sigma = alphabet

        # Defines the states, and their atributes
        self.states = states
        self.start = self.define_start_state()
        self.final = self.define_final_state()
        self.current_state = self.start

        # Defines the transition funcion that defines the automata
        self.delta = transition_function
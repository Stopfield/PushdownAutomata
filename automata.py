import networkx as nx
import matplotlib.pyplot as plt

automata = nx.DiGraph()

automata.add_node('q0', state='start state')
automata.add_node('q1')
automata.add_node('qf', state='final state')

# edge_list = [('q0', 'q0'), ('q0', 'q1'), ('q1', 'q1'), ('q0', 'qf'), ('q1', 'qf')]
# automata.add_edges_from(edge_list)

automata.add_edge('q0', 'q0', accept = '(a, void, B)')
automata.add_edge('q0', 'q1', accept = '(b, B, void)')
automata.add_edge('q0', 'qf', accept = '(?, ?, void)')
automata.add_edge('q1', 'q1', accept = '(b, B, void)')
automata.add_edge('q1', 'qf', accept = '(?, ?, void)')

print(automata.nodes)
print(automata.edges)

plt.subplot(111)
nx.draw(automata)
plt.show()
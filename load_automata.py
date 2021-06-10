# Biblioteca Regex.
import re

# Função de leitura do arquivo do autômato.
def load_file():
    # Abre o arquivo para a leitura dos componentes do autômato.
    file = open('file.txt', 'r').readline()

    # Regex para remoção de símbolos inúteis.
    regex = re.compile(r'[^a-zA-Z0-9]+')

    # Loop que separa os conjuntos em tuplas.
    arr = []
    for i in file.split(','):
        if '{' in i and not '}' in i:
            sub = []
            sub.append(regex.sub('', i))
        elif '}' in i and not '{' in i:
            sub.append(regex.sub('', i))
            sub = tuple(sub)
            arr.append(sub)
            sub = []
        elif len(sub) != 0:
            sub.append(regex.sub('', i))
        else:
            arr.append(regex.sub('', i))

    # Tratamento de erros do arquivo.
    if file.count(',') != file.count(' '):
        raise Exception("Erro na separacao dos componentes!")
    elif len(arr) != 6:
        raise Exception("Erro nos componentes do automato!")
    elif 'D' not in arr:
        raise Exception("Erro na letra do conjunto de regras de producao!")
    else:
        print(tuple(arr))

    # Abre o arquivo para a leitura das funções de transição.
    file = open('file.txt', 'r').read().splitlines()

    # Loop que separa as funções em tuplas.
    arr = []
    for i in file[1:]:
        arr.append(tuple([c.strip() for c in i.split(',')]))

    print(tuple(arr))


print(load_file())

# Saída => [('a', 'b'), ('q0', 'q1', 'q2', 'q3'), 'D', 'q0', ('q3'), ('A', 'B')]
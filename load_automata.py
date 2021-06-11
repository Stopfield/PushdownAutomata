# Biblioteca Regex.
import re

# Abre o arquivo para a leitura dos componentes e funções de transição do autômato.
file = open('file.txt', 'r').read().splitlines()

def components():
    # Regex para remoção de símbolos inúteis.
    regex = re.compile(r'[^a-zA-Z0-9]+')

    # Loop que separa os conjuntos em tuplas.
    component = []
    for i in str(file[:1]).split(','):
        if '{' in i and not '}' in i:
            aux = []
            aux.append(regex.sub('', i))
        elif '}' in i and not '{' in i:
            aux.append(regex.sub('', i))
            component.append(tuple(aux))
            aux = []
        elif len(aux) != 0:
            aux.append(regex.sub('', i))
        else:
            component.append(regex.sub('', i))

    # Tratamento de erros do arquivo.
    if file.count(',') != file.count(' '):
        raise Exception("Erro na separacao dos componentes!")
    elif len(component) != 6:
        raise Exception("Erro nos componentes do automato!")
    elif 'D' not in component:
        raise Exception("Erro na letra do conjunto de regras de producao!")
    else:
        return tuple(component)

def functions():
    # Loop que separa as funções de transição em tuplas.
    function = []
    for line in file[1:]:
        function.append(tuple([c.strip() for c in line.split(',')]))

    return tuple(function)

# print(components())
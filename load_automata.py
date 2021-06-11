# Biblioteca Regex.
import re

# Abre o arquivo para a leitura dos componentes e funções de transição do autômato.
# file = open('file.txt', 'r').read().splitlines()

def components(file):
    # Regex para remoção de símbolos inúteis.
    regex = re.compile(r'[^a-zA-Z0-9]+')

    # Tratamento de erro no arquivo.
    if file[0].count(',') != file[0].count(' '):
        raise Exception("Erro na separacao dos componentes!")

    # Loop que separa os conjuntos em tuplas.
    component = []
    for word in str(file[:1]).split(','):
        if '{' in word and not '}' in word:
            aux = []
            aux.append(regex.sub('', word))
        elif '}' in word and not '{' in word:
            aux.append(regex.sub('', word))
            component.append(tuple(aux))
            aux = []
        elif len(aux) != 0:
            aux.append(regex.sub('', word))
        else:
            component.append(regex.sub('', word))

    # Tratamento de padrão dos componentes.
    for i in component[1]:
        if not re.match(r'q[0-9]', i):
            raise Exception('Erro no padrao dos estados!')
    for i in component[0]:
        if not re.match(r'[a-z]', i):
            raise Exception('Erro no padrao dos simbolos!')
    for i in component[5]:
        if not re.match(r'[A-Z]', i):
            raise Exception('Erro no padrao dos simbolos!')
    if 'D' != component[2]:
        raise Exception('Erro na letra do conjunto de regras de producao!')
    else:
        return tuple(component)
      
def functions(file):
    # Loop que separa as funções de transição em tuplas.
    function = []
    for line in file[1:]:
        function.append(tuple([c.strip() for c in line.split(',')]))

    # Tratamento de padrão das funções de transição.
    for line in function:
        for word in line:
            if not re.match(r'[a-zA-Z0-9?-]', word):
                raise Exception("Erro: Funcao de Transicao.")
    return tuple(function)
import pandas as pd
from pandas import Series, DataFrame

# Series é um objeto tipo array unidimensional que contem uma sequencia de valores (Semelhante a tipos NumPy)
# Uma Series simples é formada por apenas um array de dados
obj = Series([3, 4, -2, 3])
print("Series simples: \n", obj, "\n")
"""
Desde que não seja específicado um index para um valor específico, por padrao, é criado uma lista de inteiros
de 0 a N - 1 (Com N sendo o tamanho desse objeto Series) e printado juntamente como valor respectivo de dado.
"""
# .values recupera os valores do objeto Series
print("Valores de obj: ", obj.values)
# .index recupera o alcance do index, tipo range(index)
print("Index de obj: ", obj.index,"\n")

# As vezes é necessário crirar um objeto tipo Series com um index identificando cada ponto de dados com um rótulo.
# Para isso, pode-se usar o seguinte comando
obj2 = Series([4, 5, -6, 7], index=['a', 'd', 'b', 'c'])
print("Obj2 com index rotulado: \n", obj2)
print("Index de obj2: ", obj2.index,"\n")
print("Selecionando dado de obj2 por index: ", obj2['a'])
print("\nSelecionando dados de obj2 por index:\n", obj2[['a', 'd', 'c']]) # Lembrar de usar dois cochetes

# Apesar de operações como: Filtragem por booleanos, Multiplicação de escalares ou aplicando funções matemáricas
# o valor de index será presenvado

# Outro jeito de pensar sobre Series é como um dicionario com tamanho fixo e ordenado. É possível usar o objeto Series
# em muitos contextos onde voce usaria dicionários

# É possível criar um objeto tipo Series a partir de um dicionário:
dictData = {"Ohio": 35000, 'Texas':71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(dictData)
print("Objeto Series a partir de um dict:\n", obj3)

# Quando vc usa dicionários, as key viram seu index rotulado e são ordenadas
# É possível sob-escrever esses index, utilizando a ferramenta de definir index
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(dictData, states)
print("Obj4 com index definidos manualmente:\n", obj4)
# Note que isso funcionou como um filtro, pois como California não pertencia ao dict, foi atribuido NaN (not a number)
# E ohio que não foi citada não foi trazida para esse novo obj4

# As funções .isnull e .notnull devem sem usadas para identificar se possui algum dado com valor vazio
print("\nVerificando se dados são vaizo em obj4:\n", obj4.isnull())
print("Verificando se dados não são vaizo em obj4:\n", obj4.notnull())

# É possívle nomear um objeto tipo Series e seu index
obj4.name = 'population'
obj4.index.name = 'state'
print("obj4 com nome de objeto e index definidos:\n", obj4)

# Um index de Series é possivel alterar utilizando o comando:
obj.index = ['Bob','Esponja','Jorge','Mateus']
print("\nObj com index alterados:\n",obj)

"""
Data Frame
    Representa uma tabela retangular de dados e contem um coleção ordenada de colunas, cada uma podendo ser um tipo 
    diferente de valor (num, str, bool, ...).
    O DataFrame possui ambos index de Coluna e Linha. Isso pode ser pensado como sendo um dicionário de Series todas 
    dividindo o mesmo index. 
    Os dados são armazenados como blocos uni ou multi dimencional tipo uma list dict ...
"""
# Há muito jeito de construir um DatFrame, um dos mais utilizados é criar a partir de um dicionário de lista ou Numpy
# arrays de mesmo tamanho.
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = DataFrame(data)
print("DataFrame:\n", frame)

# .head() seleciona apenas as 5 primeiras linhas

# Se caso especificar as colunas, o DataFrame vai organizar em ordem que foi passada pelo user
frame2 = DataFrame(data, columns=['year', 'state', 'pop'], index=['one', 'two', 'three', 'four', 'five', 'six'])
print("\nDataFrame2 organizado as colunas pelo user:\n", frame2)
# Se caso passar um valor de coluna que não existe ele vai mostar na tabelea como NaN (Not a number)
# Os valores das colunas de um DataFrame podem ser acessados como atributo
print("Acesso DataFrame Colunas como atributo:\n", frame2.year)
# Pode-se acessar a linha pelo [index] ou pelo método .loc[index]
print("Linha 2 frame:\n", frame2.loc['three'])



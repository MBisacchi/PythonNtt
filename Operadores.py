# - Operadores arrtiméticos - contas matemáticas
# segue as convenções das regras matemáticas (ex.: 1. (), 2. expoentes, 3. * e /, 4. + e -)

# Adição
print (1+1)

# Subtração
print (10-2)

# Multiplicação
print (4*3)

# Divisão quebrada 
print (12/3)

# Divisão inteira
print (12//2)

# Modulo -> resto da divisão
print (10%3)

# Exponenciação -> o numero (x=2) ao cubo ou ao qudrado
print (2**3)



# - Opreadores de comparação - comparar valores

varSaldo = 10
varSaque = 5

# é igual
print (varSaldo == varSaque)

# é diferente
print (varSaldo != varSaque)

# Maior ou maior igual que
print (varSaldo > varSaque)
print (varSaldo >= varSaque)

# menor ou menor igual que
print (varSaldo < varSaque)
print (varSaldo <= varSaque)



# - Operadores de atribuição - são utilizados para um valor inicial ou sobrescrever a variável

# Atribuição simples
varSimples = 1

# Atribuição com operação - serve com todas as operações 
exAdicao = 0
exAdicao += 2



# - Operadores lógicos - Serve para comparar as variáveis de uma expressão
print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)

exLogico1 = 1000
exLogico2 = 250
exLogico3 = 200

# and (e) - juntas as expressões, as respostas das operações tem que ser verdadeiras para dar true
expAnd = exLogico1 == 1000 and exLogico2 >= 249
print ('And:')
print (expAnd)

# or (ou) - verifica as expressões, basta uma operação ser verdade para dar true
expOr = exLogico1 == 1000 or exLogico2 == 3
print ('Or:')
print (expOr)

# not (não) - inverso da operação (pode negar valores, listas e string )
expNot = not 10 > 15
print ('Not:')
print (expNot)

# Parênteses - Delimita a precedência
# na resolução é da esq, p/ dir., mas pode se usar para ficar mais légivel o código
(exLogico2 == exLogico1) or (exLogico1 > exLogico3)



#  - Operadores de identidade - Compara dois objetos testados ocupam a mesma posição de memória.
saldo, limite = 200, 200

# Comparação positiva
print ('is:')
print(saldo is limite)

# Comparação negativa
print ('is not:')
print (saldo is not limite)



# - Operadores de associação - Verificase o obj está na sequência
listNumeros = [100,50]
curso = "Python"

print('Op. associação')
print ("Python" in curso)
print('Op.associação')
print(50 not in listNumeros)


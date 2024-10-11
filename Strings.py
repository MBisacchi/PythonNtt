# - STRING - tipo de dados, abrange números, letras e caractéres.
curso = " pYthon "

# - Transformar letra 

# upper - Transforma tudo em maiúsculo
print (curso.upper())

# lower - Transforma tudo em minúsculo
print (curso.lower())

# title - Transforma a primeira letra em maiúsculo e as demais em minúsculo.
print (curso.title())

# - Remover espaços

# strip - Remove espaços em branco da esq. e dir.
print (curso.strip())

# lstrip - Remove espaço da esquerda
print (curso.lstrip())

# rstrip - Remove espaço da direita
print (curso.rstrip())

# Junções e centralização

# center - centraliza o valor da variável de acordo com o espaço definado no argumento (pode ser vazio também, sem o ponto)
print (curso.center(15,"."))

# join - a cada item da variável, ele irá colocar o ponto (argumento)
print (".".join(curso))


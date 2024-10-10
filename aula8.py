nome = 'Ana Clara'
sobrenome = 'Alves Pereira'
ano_nascimento = 2002
idade = 2024 - ano_nascimento
maior_de_idade = idade >= 18
altura = 1.73

#transformando o boolenao de True or False para Sim ou Nao
if maior_de_idade == True:
    maior_de_idade = 'Sim'
else:
    maior_de_idade = 'Nao'

print('Nome:', nome) #string
print('Sobrenome:', sobrenome) #string
print('Idade:', idade) #int
print('Ano de nascimento:', ano_nascimento) #int
print('Maior de idade?:', maior_de_idade) #bool
print('Altura (em metros):', altura) #float

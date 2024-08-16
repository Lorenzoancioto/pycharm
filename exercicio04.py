def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): # aqui temos uma função
total_notas = 0 # aqui temos uma variável e seu valor pre-escrito
num_alunos = len(notas) 0 # aqui temos uma variável e seu valor pre-escrito para os vetores abaixo
aprovados = [] 0 # aqui temos uma variável dizendo que elas sao "array", um vetor
reprovados = [] [] 0 # aqui temos uma variável dizendo que elas sao "array", um vetor

for aluno, nota in notas.items(): # um "para" um bloco que diz "para a variável aluno, que tem a sua nota dentro do array"
total_notas += nota # falando que agora o valor de "total_notas" é igual a variável "notas"
if nota >= nota_minima_aprovacao: # um bloco de condição, dizendo que se nota for maior ou igual a outra variável algo ira acontecer, porém somente se a condição for correspondida
aprovados.append(aluno) # ira adicionar a variável aluno para o array "aprovados"
else: # caso a conicional nao for correspondida então o else entra em ação
reprovados.append(aluno) # adicionando a variável aluno dentro da array " reprovado"

media_turma = total_notas / num_alunos # estamos criando uma variável para fazermos a media dos alunos

return media_turma, aprovados, reprovados # retornamos todas as variáveis presentes abaixo do else e acima do return

notas = { # aqui temos uma "geral das notas" dos alunos
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70  # uma variável que corresponde a nota minima necessaria para passar de ano/bim

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao) # mudando o valor de tres variáveis por uma so

print(f"Média da turma: {media_turma:.2f}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprenteses
print(f"Alunos aprovados: {', '.join(aprovados)}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprenteses
print(f"Alunos reprovados: {', '.join(reprovados)}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprenteses
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): # uma funçao

if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: # um bloco condicional que tem a sua condição declarada logo apos a sua menção, o qual interfere diretmente o codigo abaixo
return "Diabetes" # dependo do resultado a cima o resultado ira retornar a palavra "diabetes"
elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: # uma nova condição independente se a condição de cima fora usada ou nao
return "Pré-diabetes" # dependendo do resultado do bloco de ocndição a cima teremos um resultado, o resultado sera "Pre-diabetes"
else: # um bloco de condição tambem, porem este sera usado somente se nenhum dos blocos "if" acima forem correspondidos
return "Normal"

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo, como ficou visivel nos casos dos "if"
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo, como ficou visivel nos casos dos "if"

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) # aqui ele muda o valor que esta dentro da variavel "resultado"
print(f"O diagnóstico é: {resultado}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprenteses
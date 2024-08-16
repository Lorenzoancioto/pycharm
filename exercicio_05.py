def calcular_imc(peso, altura): # uma função

imc = peso / (altura ** 2) # uma variável e a sua "formula"
return imc # ira retornar o valor do imc e deixar armazenado para ser usado pelo resto do codigo

def classificar_imc(imc): # um nova função

if imc < 18.5: # um bloco de condição que ira verificar o valor do imc caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Abaixo do peso" # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas
elif 18.5 <= imc < 24.9: # um bloco de condição que ira verificar o valor do imc caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Peso normal" # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas
elif 25 <= imc < 29.9: # um bloco de condição que ira verificar o valor do imc caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Sobrepeso" # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas
elif 30 <= imc < 34.9: # um bloco de condição que ira verificar o valor do imc caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Obesidade grau 1" # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas
elif 35 <= imc < 39.9: # um bloco de condição que ira verificar o valor do imc caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Obesidade grau 2" # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas
else: # caso nenhum dos "if" seja correspondido entao o else entra em ação, é um bloco de condição tambem
return "Obesidade grau 3" # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

def sugestao_atividade_fisica(classificacao_imc): # uma nova função

if classificacao_imc == "Abaixo do peso": # um bloco de condição que ira verificar o valor de classificacao_imc, caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."  # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

elif classificacao_imc == "Peso normal": # um bloco de condição que ira verificar o valor de classificacao_imc, caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."  # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

elif classificacao_imc == "Sobrepeso": # um bloco de condição que ira verificar o valor de classificacao_imc, caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."  # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

elif classificacao_imc == "Obesidade grau 1": # um bloco de condição que ira verificar o valor de classificacao_imc, caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."  # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

elif classificacao_imc == "Obesidade grau 2": # um bloco de condição que ira verificar o valor de classificacao_imc, caso seja correspondido o return entra em ação, caso contrário segue ate chegar no else
return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."  # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

else: # caso nenhum dos "if" seja correspondido entao o else entra em ação, é um bloco de condição tambem
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista." # irá retrornar uma mensagem na tela do usuário com o que esta entre aspas

peso = float(input("Digite seu peso (em kg): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo
altura = float(input("Digite sua altura (em metros): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo

imc = calcular_imc(peso, altura) # muda o valor das variáveis para o que esta entre parenteses
classificacao_imc = classificar_imc(imc) # muda o valor das variáveis para o que esta entre parenteses
sugestao = sugestao_atividade_fisica(classificacao_imc) # muda o valor das variáveis para o que esta entre parenteses

print(f"Seu IMC é: {imc:.2f}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprentes
print(f"Classificação: {classificacao_imc}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprentes
print(f"Sugestão de atividade física: {sugestao}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprentes
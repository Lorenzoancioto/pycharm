def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio): # cria uma função com alguns parametros dentro dela

custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel  # uma variável e a sua "formula"

custo_pedagio_total = numero_pedagios * custo_pedagio # uma variável e a sua "formula"

custo_total = custo_combustivel_total + custo_pedagio_total # uma variável e a sua "formula"

return custo_total, custo_combustivel_total, custo_pedagio_total # uma variável e a sua "formula"

distancia = float(input("Digite a distância da viagem (em km): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo, como ficou visivel nos casos dos "if"
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo, como ficou visivel nos casos dos "if"
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo, como ficou visivel nos casos dos "if"
numero_pedagios = int(input("Digite o número de pedágios no percurso: ")) # aqui ele cria uma variável para que o usuário possa inserrir alguma informações que seram usadas no codigo, como ficou visivel nos casos dos "if"
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,custo_combustivel,consumo_veiculo, numero_pedagios,custo_pedagio) # ira mudar o valor que esta dentro das variáveis para o que esta dentro dos parenteses

print(f"Custo total da viagem: R${custo_total:.2f}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprentes
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprentes
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}") # aqui o sistema ira exibir uma mensagem na tela do usuário dizendo tudo aquilo que esta entre os aprentes
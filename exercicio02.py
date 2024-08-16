def calcular_area_comodos(): #uma função
total_area = 0 # um avariável com valor inicial igual a 0
while True: # um "laço de repetição - while" fizendo que em quanto "True" faça algo

largura = float(input("Digite a largura do cômodo (em metros): ")) # uma variável para ter seu valor inserido pelo usuario e integrada ao sistema
comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) # uma variável para ter seu valor inserido pelo usuario e integrada ao sistema

area_comodo = largura * comprimento # uma variável e a sua "fórmula"
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") # ira imprimir um resultado na tela do usuário com as informa~çoes que estão dentro do parenteses

total_area += area_comodo # uma variável e a sua formula

mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() # uma variavel que tera uma informação inserida dentro do sistema
if mais_comodos != 's': # um boco de condicional que depende totalmente do item de cima, ou seja, se "mais comodos for diferente de "s" ele ira parar o sistema
break # um bloco que ira quebrar o codigo, forçar uma parada imediata

return total_area # retornando o valor total_area como valor final

area_total = calcular_area_comodos() # esta mudando o valor contido dentro da variável "area_total"
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") # ira imprimir na tela do usuario tudo aquilo que esta entre os parenteses
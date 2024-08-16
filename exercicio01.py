def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): # temos uma função a qual tem seus tres parametros dentro dos parenteses
taxa_juros_diaria = taxa_juros_anual/365/100 # aqui uma variável e a sua "fórmula"

juros = valor_principal * taxa_juros_diaria * dias_atraso # aqui uma variável e a sua "fórmula"

valor_total = valor_principal + juros # aqui uma variável e a sua "fórmula"
return valor_total, juros # aqui temos um return que ira devolver ao sistema valor_total e o juros

valor_principal = 1000.00 # aqui estamos inserindo direto no programa qual o valor do "valor principal"
taxa_juros_anual = 5.0 # aqui estamos inserindo direto no programa qual o valor do "taxa_juros_anual"
dias_atraso = 30  # aqui estamos inserindo direto no programa qual o valor do "dias_atraso"
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
print(f"Valor total a ser pago: R${valor_total:.2f}") # ira imprimir na tela o que esta entre aspas, porém o numero tera somente duas casa decimais
print(f"Valor dos juros: R${juros:.2f}") # ira imprimir na tela o que esta entre aspas, porém o numero tera somente duas casa decimais
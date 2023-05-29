#Preço de Custo / Preço de Venda

preco_Custo = float (input("Informe o preço de custo do produto: "))
percentual = float (input("Informe o percentual adcional do produto: "))

valor_Venda = preco_Custo + (preco_Custo * percentual/100)

print ("Valor de venda do produto: ", valor_Venda)
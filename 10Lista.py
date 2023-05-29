#Custo de fábrica/Custo ao consumidor

custo_Fabrica = float (input("Informe o custo de fábrica do carro: "))

impostos = custo_Fabrica + (custo_Fabrica * 0.45)
percentagem = impostos + (impostos * 0.28)

print ("Custo ao consumidor: ", percentagem)
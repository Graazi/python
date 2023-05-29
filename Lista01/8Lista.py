#Nome/Salário fixo/Salário no final do mês.

nome = str (input("Informe o nome do vendedor: "))
salario_Fixo = float (input("Informe o salário fixo do vendedor: "))
total_Vendas = float (input("Informe o total de vendas (em dinheiro) do vendedor: "))

salario_Final = salario_Fixo + (total_Vendas * 0.15)

print (nome, "Salário fixo:", salario_Fixo, "Salário no final do mês:", salario_Final)
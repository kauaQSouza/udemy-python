valor_fixo = 500
comissao = 0.06
vendas_no_mes = float(input("digite o seu total de vendas no mes: "))

faturamento = valor_fixo + comissao * vendas_no_mes
print(faturamento)
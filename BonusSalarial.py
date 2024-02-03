print("Cálculo de Salário")
salario = float(input("Informe seu salário: "))
print("Salário: ",salario)

tempoS = float(input("Informe o tempo de serviço: "))

if tempoS > 5:
    print("Bônus adicional de 5% R$: ",salario*0.05)
else:
    print("Sem bônus adicional :(")    
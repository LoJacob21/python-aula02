print("Cálculo da compra final")

valorCompra = float(input("Informe o valor da compra R$: "))

print("Escolha a forma de pagamento")
print("C - Crédito")
print("D - Débito")
formaPag = input("Escolha: ")

print("Escolha uma opção de parcelamento caso necessário")
print("Até 10x sem juros")
print("Até 18x vezes com juros")
parcelas = int(input("Parcelar em : "))

if formaPag == "D":
    if valorCompra > 1000:
        ValorFinal = valorCompra - (valorCompra*0.2)
    elif valorCompra > 500:
        ValorFinal = valorCompra - (valorCompra*0.15) 
    else:
        ValorFinal = valorCompra - (valorCompra*0.1)    

if formaPag == "C":
    if valorCompra < 800 and parcelas > 5:
        print("Quantidade de parcelas inválidas!")
        exit() #encerra o programa
    elif parcelas > 10:
        if parcelas == 11:
            Juros = 0.05 
        elif parcelas == 12:
            Juros = 0.065
        elif parcelas == 13:
            Juros = 0.07
        elif parcelas == 14:
            Juros = 0.09
        elif parcelas == 15:
            Juros = 0.095
        elif parcelas == 16:
            Juros = 0.1
        elif parcelas == 17:
            Juros = 0.113
        elif parcelas == 18:
            Juros = 0.12
        else:
            print("Inválido!!")
            exit()                      

ValorFinal = (valorCompra/parcelas) + (valorCompra * Juros)  

print("Resultado final: ", ValorFinal)
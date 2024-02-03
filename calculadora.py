numero1 = float(input("Numero 1: "))
numero2 = float(input("Numero 2: "))

print("Escolha uma operação: +Adição, -Subtração, /Divisão, *Multiplicação")
operacao = input("+ - / *: ")

if operacao == '+':
    print(f"Resultado = {numero1+numero2}")
elif operacao == '-':
    print(f"Resultado = {numero1-numero2}")
elif operacao == '/':
    if(numero2 == 0):
        print("Não é possível dividir por zero")
    else:
        print(f"Resultado = {numero1/numero2}")    
elif operacao == '*':
    print(f"Resultado = {numero1*numero2}") 
else:
    print("Erro!")           




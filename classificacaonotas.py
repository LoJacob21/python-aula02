nota = float(input("Informe o valor da nota (0 a 100): "))
print("Nota: ",nota)

if nota > 100 and nota < 0:
    print("Nota inválida!")
elif nota >= 90: 
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")               
num1 = int(input ("Digite um Numero: "))

num2 = input ("Digite outro Numero: ")
num2 = int(num2)

print("Soma:\t\t", num1+num2)
print(f"Subtração:\t{num1-num2}")
print(f"Multiplicação:\t{num1*num2}")

if num2!=0:
    print(f"Divisão:\t{num1/num2}")
else: # num2==0
    print("Não existe divisão por zero")
m = int(input("Qual a medida de temperatura de entrada? \n1 - Celsius \n2 - Farenheit \n3 - Kelvin\n"))
temp = float(input("Digite a temperatura para conversão: "))

if m == 1:

    c = int(input("Qual a medida de saída?\n1 - Farenheit\n2 - Kelvin "))

    if c == 1:
        cf = (temp * 9/5) + 32
        print(cf)
    
    elif c == 2:
        ck = (temp + 273.15)
        print(ck)
    
    else:
        print("Opção inválida")
        

elif m == 2:

    f = int(input("Qual a medida de saída?\n1 - Celsius\n2 - Kelvin "))
    
    if f == 1:

        fc = (temp - 32) * 5/9
        print(fc)

    elif f == 2:

        fk = (temp - 32) * 5/9 + 273.15
        print(fk)

    else:
        
        print("Opção inválida")

elif m == 3:

    k = int(input("Qual a medida de saída?\n1 - Celsius\n2 - Farenheit "))
    
    if k == 1:

        kc = temp - 273.15
        print(kc)

    elif k == 2:

        kf = (temp - 273.15) * 9/5 + 32
        print (kf)

    else:
        
        print("Opção inválida")

else:
    print("Opção inválida")
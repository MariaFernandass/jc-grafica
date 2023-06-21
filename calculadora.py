while(True):
    print("1. Somar", "2. Subtrair","3. Multiplicar", "4. Dividir", "5. Sair", sep="\n")
    op = int(input("Escolha uma opção: ")) 
    if op<1 or op>5:
        print("Opção Inválida")
        continue
    elif op == 5:
        break
    n = int(input("Digite o primeiro número: "))
    m = int(input("Digite o segundo número: "))

    if op == 1:
        print(f"{n}+{m} = {n+m}")
    elif op == 2:
        print(f"{n}-{m} = {n-m}")
    elif op == 3:
        pass
    else:
        pass
    print("Até logo!")
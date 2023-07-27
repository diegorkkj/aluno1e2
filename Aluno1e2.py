x = "n"

while x !="y":

    nome1 = input("Informe o seu nome aluno 1: ")

    idade1 = int(input(f"Informe a sua idade {nome1}: "))
 
    nome2 = input("Informe seu nome aluno 2: ")

    idade2 = int(input(f"Informe a sua idade {nome2}: "))

    idadet = idade1 + idade2

    if idade1 > idade2:
        print(f"O aluno 1 é o {nome1}, e o aluno 2 é o {nome2}.")
        print(f"O {nome1} é mais velho que o {nome2}.")
        print(f"A soma das idades é {idadet}.")
    else:
        print(f"O aluno 1 é o {nome1}, e o aluno 2 é o {nome2}.")
        print(f"O {nome2} é mais velho que o {nome1}.")
        print(f"A soma das idades é {idadet}.")

    x = input("Deseja sair? \n y = SIM \n n = NÃO \n")
    if x == "Y" or x == "sim":
        x = "y"
    elif x == "N" or x == "não":
        x = "n"
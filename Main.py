
while True:
    try:
        cpf=input("Digite um cpf:")
        if cpf.lower()=="sair":
            break
        cpf=int(cpf)
        print(f'{cpf:0>11}',end='')
        if validar_cpf(cpf)==True:
            print(' válido!')
        else:
            print(' inválido!')
    except:
        print(f'{cpf} não é um valor aceito')
        

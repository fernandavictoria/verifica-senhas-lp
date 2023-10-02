#Fernanda Victoria de Sousa - 2 informatica
print("Verificando a força das suas senhas senhas")
senhas=input("Digite as senhas a para verificar sua força \n (as senhas serão separadas com espeço)").split()
results=[]

for senha in senhas:
    comprimento=len(senha)>=8
    maiuscula=False
    minuscula=False
    num=False
    caracter=False

    for s in senha:
        if s.isupper():
            maiuscula=True
        if s.islower():
            minuscula=True
        if s.isdigit():
            num=True
        if s in "!@#$%^&*()_+-=[]{}|;:,.<>?/":
            caracter=True

    verifica=   (
        comprimento
        and maiuscula
        and minuscula
        and num
        and caracter
    )

    results.append(verifica)

print(results)
entrada = input("Digite uma palavra: ")

# Forma facil
invertida = entrada[::-1]

# Forma com laço de repetição
invertida2 = []
for i in range(len(entrada)-1, -1, -1):
    invertida2.append(entrada[i])

#print("Palavra invertida:", invertida)
invertida2 = ''.join(invertida2)
print("Palavra invertida:", invertida2)
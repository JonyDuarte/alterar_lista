# lista
nomes = ["João", "Gabriela", "Agnes", "Ian", "Futrico", "Alissom", "Eunice", "Isaura"]

# exibir a lista
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}")

# usuario informa o indice que deseja alterar
try:
    indice = int(input("Informe o número do índice que deseja alterar: "))
    confirmacao = input(f"Deseja alterar o nome {nomes[indice]}? Digite 'sim' para confirmar: ")

    if confirmacao == "sim":
        novo_nome = input("Informe o novo nome: ")
        nomes[indice] = novo_nome
    else: 
        ...
except Exception as e:
    print(f"Não foi possível alterar o nome. {e}.")

finally:
      # nova lista
     for i in range(len(nomes)):
        print(f"Índice {i}: {nomes[i]}.")
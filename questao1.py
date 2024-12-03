continentes = {
    0: ("América do Norte", "North America"),
    1: ("África", "Africa"),
    2: ("Europa", "Europe"),
    3: ("Ásia", "Asia"),
    4: ("Oceania", "Oceania"),
    5: ("Antártida", "Antarctica"),
    6: ("América do Sul", "South America")
}

print("Escolha um Continente para traduzir")

# lista pra escolher
for i, (nome_pt, nome_en) in continentes.items():
    print(f"{i}: {nome_pt}")

print(" ") # espaço em branco

try:
    escolha = int(input("Digite o número do continente: "))
    print(" ") # espaço em branco

    # verificação da escolha
    if escolha in continentes:
        nome_pt, nome_en = continentes[escolha]
        print(f"{nome_pt} === {nome_en}\n")
    else:
        print("Escolha apenas entre 0 e 6!!!!!!!")

except ValueError:
    print("Você precisa digitar um número!!!!!!!!!")

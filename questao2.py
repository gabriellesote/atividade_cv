import requests

try:
    continentes = ["Africa", "North America", "Asia", "Europe", "South America", "Oceania"]
    print("Continentes Disponiveis para consulta: ")

    for i, continente in enumerate(continentes):
        print(f"{i}: {continente}")

    escolha = input("Escolha o continente: ").strip().capitalize()   

    if escolha not in continentes:
        print("Continente não disponível na lista.")
    else:
        url = f"https://disease.sh/v3/covid-19/continents/{escolha}"

        response = requests.get(url)

   
        if response.status_code == 200:
            data = response.json()

            casos = data.get("cases")
            deaths = data.get("deaths")
            hoje = data.get("todayCases")
            print(f"Covid no {escolha}:  -casos: {casos}  - mortes: {deaths}  - Casos de hoje: {hoje}")
        else:
            print(f"Erro {response.status_code}: Continente não encontrado no API.")

except requests.exceptions.RequestException as e:
    print(f"Erro de requisição: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
import json
import requests

# URL da API OLX com pesquisa por "peças carro"
URL = "https://www.olx.pt/api/v1/offers/?limit=20&offset=0&query=pe%C3%A7as%20carro&sorting=desc-relevance"

# Cabeçalhos para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

print("A aceder à API OLX com pesquisa...")
response = requests.get(URL, headers=headers)

# Verifica se a resposta foi bem-sucedida
if response.status_code != 200:
    print(f"Erro ao aceder à API. Status: {response.status_code}")
    print(response.text)
    exit()

data = response.json()
anuncios = data.get("data", [])

print(f"Encontrados {len(anuncios)} anúncios.")
items = []

# Processar os anúncios
for anuncio in anuncios:
    try:
        titulo = anuncio["title"]

        # Preço
        if "price" in anuncio and "value" in anuncio["price"] and "display" in anuncio["price"]["value"]:
            preco = anuncio["price"]["value"]["display"]
        else:
            preco = "Preço não disponível"

        # Localização
        if "location" in anuncio and "city_name" in anuncio["location"]:
            local = anuncio["location"]["city_name"]
        else:
            local = "Localização desconhecida"

        # Imagem com correções
        imagem = anuncio["photos"][0]["link"] if anuncio.get("photos") else ""
        imagem = imagem.replace(":443", "")          # Remove :443
        imagem = imagem.split(";")[0]                # Remove parâmetros como ;s={width}x{height}

        # Link do anúncio
        if "slug" in anuncio:
            link = "https://www.olx.pt/d/anuncio/" + anuncio["slug"]
        else:
            link = f"https://www.olx.pt/redirect/?id={anuncio['id']}"

        # Adicionar ao array
        items.append({
            "nome": titulo,
            "descricao": f"Localização: {local}",
            "preco": preco,
            "imagem": imagem,
            "link": link
        })

    except Exception as e:
        print(f"Erro ao processar anúncio: {e}")
        continue

# Guardar os dados em data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Guardado {len(items)} itens em data.json")

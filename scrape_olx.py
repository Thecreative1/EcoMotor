import requests
from bs4 import BeautifulSoup
import json

def scrape_olx_motores():
    url = "https://www.olx.pt/carros-motos-e-barcos/pecas-auto-acessorios/motores/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = []
    for ad in soup.select('div[data-cy="l-card"]'):
        try:
            nome = ad.select_one("h6").text.strip()
            preco = ad.select_one("p[data-testid='ad-price']").text.strip()
            local = ad.select_one("p[data-testid='location-date']").text.strip().split(" - ")[0]
            link = "https://www.olx.pt" + ad.find("a")["href"]
            imagem = ad.find("img")["src"]

            items.append({
                "nome": nome,
                "descricao": "Motor usado",
                "preco": preco,
                "localizacao": local,
                "origem": "OLX",
                "imagem": imagem,
                "link": link
            })
        except Exception as e:
            print("Erro OLX:", e)

    with open("data_olx.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    print(f"{len(items)} motores do OLX guardados.")

scrape_olx_motores()

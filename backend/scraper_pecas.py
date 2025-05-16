import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "https://www.olx.pt/carros-e-cacifos/pecas-acessorios/"
MAX_ITEMS = 20
TEMPO_ESPERA = 5

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get(BASE_URL)
time.sleep(TEMPO_ESPERA)

items = []
anuncios = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="listing-grid"] a.css-rc5s2u')
print(f"Encontrados {len(anuncios)} anúncios.")

for anuncio in anuncios[:MAX_ITEMS]:
    try:
        titulo = anuncio.find_element(By.CSS_SELECTOR, 'h6').text
        preco = anuncio.find_element(By.CSS_SELECTOR, 'p[data-testid="ad-price"]').text
        local = anuncio.find_element(By.CSS_SELECTOR, 'p[data-testid="location-date"]').text.split(" - ")[0]
        imagem_tag = anuncio.find_element(By.CSS_SELECTOR, 'img')
        imagem = imagem_tag.get_attribute('src')
        link = anuncio.get_attribute('href')

        items.append({
            "peca": titulo,
            "marca": "",  # Podes extrair da descrição depois
            "modelo": "",
            "preco": preco,
            "estado": "Usado",  # Valor genérico, melhor se scrapearmos detalhe
            "localizacao": local,
            "imagem": imagem,
            "link": link
        })
    except Exception as e:
        print(f"Erro num anúncio: {e}")
        continue

driver.quit()

# Guardar ficheiro
with open("pecas.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Guardado {len(items)} itens em pecas.json")

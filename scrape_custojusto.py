from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

def scrape_custojusto_selenium():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    url = "https://www.custojusto.pt/portugal/motores?o=1"
    driver.get(url)
    time.sleep(4)  # Esperar o carregamento inicial

    # Guardar HTML para debug
    html = driver.page_source
    with open("custojusto_dump.html", "w", encoding="utf-8") as f:
        f.write(html)

    anuncios = driver.find_elements(By.CSS_SELECTOR, "li[data-testid='listing-ad']")
    print(f"🔍 {len(anuncios)} anúncios encontrados no CustoJusto")

    items = []
    for ad in anuncios:
        try:
            nome = ad.find_element(By.TAG_NAME, "h2").text.strip()
            preco = ad.find_element(By.CLASS_NAME, "price").text.strip()
            local = ad.find_element(By.CLASS_NAME, "location").text.strip()
            link = ad.find_element(By.TAG_NAME, "a").get_attribute("href")
            imagem_tag = ad.find_element(By.TAG_NAME, "img")
            imagem = imagem_tag.get_attribute("src") if imagem_tag else ""

            items.append({
                "nome": nome,
                "descricao": "Motor usado",
                "preco": preco,
                "localizacao": local,
                "origem": "CustoJusto",
                "imagem": imagem,
                "link": link
            })
        except Exception as e:
            print("⚠️ Erro num anúncio:", e)

    driver.quit()

    with open("data_custojusto.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    print(f"✅ {len(items)} anúncios guardados em data_custojusto.json")

if __name__ == "__main__":
    scrape_custojusto_selenium()

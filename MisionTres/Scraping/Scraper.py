import requests
from bs4 import BeautifulSoup
import csv

# URL del sitio web que queremos scrapear
url = "https://perfumesreal.com/"  # Reemplaza con la URL real


# Hacer la solicitud GET
response = requests.get(url)

# Verificar el código de estado
if response.status_code == 200:
    page_content = response.text

    # Parsear el contenido HTML
    soup = BeautifulSoup(page_content, 'html.parser')

    # Encontrar y extraer los títulos de los productos
    #Remplazar la clase y etiqueta
    product_elements = soup.find_all('div', class_='t4s-product-info')

    products = []

    for product_element in product_elements:
        title_element = product_element.find('h3', class_='t4s-product-title')
        price_element = product_element.find('div', class_='t4s-product-price')

        if title_element and price_element:
            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True)
            products.append({'Title': title, 'Price': price})

    # Guardar los productos en un archivo CSV
    with open('.\Misión Tres\Scraping\products.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

    print("Datos guardados en products.csv")
else:
    print(f"Error: {response.status_code}")


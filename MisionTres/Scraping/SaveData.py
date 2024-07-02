import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import ttk, messagebox

def scrape_data():
    url = url_entry.get()
    title_class = title_class_entry.get()
    price_class = price_class_entry.get()

    if not url or not title_class or not price_class:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, 'html.parser')

        product_elements = soup.find_all('div', class_='t4s-product-info')
        products = []

        for product_element in product_elements:
            title_element = product_element.find('h3', class_=title_class)
            price_element = product_element.find('div', class_=price_class)
            
            if title_element and price_element:
                title = title_element.get_text(strip=True)
                price = price_element.get_text(strip=True)
                products.append({'Title': title, 'Price': price})

        with open('products.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
            writer.writeheader()
            for product in products:
                writer.writerow(product)

        messagebox.showinfo("Éxito", "Datos guardados en products.csv")
    else:
        messagebox.showerror("Error", f"Error: {response.status_code}")

# Configuración de la interfaz Tkinter
root = tk.Tk()
root.title("Web Scraping con Tkinter")

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Variables de entrada
url = tk.StringVar()
title_class = tk.StringVar()
price_class = tk.StringVar()

# Etiquetas y campos de entrada
ttk.Label(mainframe, text="URL:").grid(column=1, row=1, sticky=tk.W)
url_entry = ttk.Entry(mainframe, width=50, textvariable=url)
url_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Clase del título:").grid(column=1, row=2, sticky=tk.W)
title_class_entry = ttk.Entry(mainframe, width=50, textvariable=title_class)
title_class_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Clase del precio:").grid(column=1, row=3, sticky=tk.W)
price_class_entry = ttk.Entry(mainframe, width=50, textvariable=price_class)
price_class_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

# Botón para iniciar el scraping
ttk.Button(mainframe, text="Extraer Datos", command=scrape_data).grid(column=2, row=4, sticky=tk.E)

# Configuración de padding para los elementos del grid
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()

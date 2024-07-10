# Análisis de Ventas Mensuales

## Descripción del Problema

Una tienda registra las ventas diarias y quiere analizar estos datos para obtener una visión clara de las ventas mensuales. Este análisis ayudará a identificar meses con ventas altas o bajas, permitiendo ajustar estrategias de negocio en consecuencia.

### Objetivos

1. **Cargar y Procesar Datos**: Leer los datos de ventas desde un archivo CSV.
2. **Agregación de Ventas Mensuales**: Calcular el total de ventas para cada mes.
3. **Visualización de Datos**: Generar un gráfico que muestre las ventas mensuales para facilitar la interpretación visual de los datos.

## Estructura del Proyecto

El proyecto se organiza en los siguientes archivos:
```
RegistroVentas/
├── main.py
├── sales_analysis.py
├── Generador.py
└── sales_data.csv
```


- `main.py`: Módulo principal que ejecuta el flujo del análisis.
- `sales_analysis.py`: Módulo auxiliar que contiene las funciones para cargar datos, calcular ventas mensuales y generar gráficos.
- `Generador.py`: Módulo generador de datos  con registros de ventas.
- `sales_data.csv`: Archivo de datos de ejemplo con registros de ventas.


## Configuración del Proyecto

### Instalar Dependencias:
Asegúrate de tener instalados pandas y matplotlib. Puedes instalarlos usando pip:

```bash
pip install pandas matplotlib
```

## Contenido de `Generador.py`

Este módulo contiene las siguientes funciones:

```python
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales_data(start_date, end_date, output_file):
    """
    Genera datos de ventas diarias y los guarda en un archivo CSV.

    :param start_date: Fecha de inicio (YYYY-MM-DD)
    :param end_date: Fecha de fin (YYYY-MM-DD)
    :param output_file: Nombre del archivo CSV de salida
    """
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    sales = [random.randint(100, 3000) for _ in range(len(dates))]
    
    sales_data = pd.DataFrame({
        'Date': dates,
        'Sales': sales
    })
    
    sales_data.to_csv(output_file, index=False)
    print(f"Datos de ventas generados y guardados en {output_file}")

# Configurar las fechas de inicio y fin para los datos simulados
start_date = '2023-01-01'
end_date = '2023-12-31'
output_file = 'D:\Shadow\GitHub\Curso-Explorador\Misión Dos\RegistroVentas\sales_data.csv'

# Generar los datos de ventas
generate_sales_data(start_date, end_date, output_file)


```

## Contenido de `sales_analysis.py`

Este módulo contiene las siguientes funciones:

```python
import pandas as pd
import matplotlib.pyplot as plt

def load_sales_data(file_path):
    """Carga datos de ventas desde un archivo CSV."""
    return pd.read_csv(file_path)

def calculate_monthly_sales(data):
    """Calcula las ventas mensuales agregadas."""
    data['Date'] = pd.to_datetime(data['Date'])
    monthly_sales = data.resample('M', on='Date').sum()
    return monthly_sales

def plot_monthly_sales(monthly_sales):
    """Genera un gráfico de las ventas mensuales."""
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales.index, monthly_sales['Sales'], marker='o')
    plt.title('Monthly Sales Analysis')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()
```
## Contenido de `main.py`

Este módulo contiene las siguientes funciones:

```python
import sales_analysis as sa

def main():
    # Ruta del archivo CSV con los datos de ventas
    file_path = 'D:\Shadow\GitHub\Curso-Explorador\Misión Dos\RegistroVentas\sales_data.csv'
    
    # Cargar datos de ventas
    sales_data = sa.load_sales_data(file_path)
    
    # Calcular ventas mensuales
    monthly_sales = sa.calculate_monthly_sales(sales_data)
    
    # Mostrar gráfico de ventas mensuales
    sa.plot_monthly_sales(monthly_sales)

if __name__ == '__main__':
    main()

```


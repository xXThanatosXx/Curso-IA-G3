import pandas as pd
import matplotlib.pyplot as plt

def load_sales_data(file_path):
    """Carga datos de ventas desde un archivo CSV."""
    return pd.read_csv(file_path)
"""La función pd.to_datetime se encarga de la conversión, 
asegurando que cualquier formato de fecha en la columna Date se interprete 
correctamente como un objeto de fecha y hora.
Esta línea usa el método resample de Pandas para agrupar los datos por mes.
El argumento 'M' indica que queremos agrupar por meses.
on='Date' especifica que la agrupación se hará basada en la columna Date.
La función sum() se aplica a cada grupo mensual, sumando las ventas de todos los días de ese mes. 
Esto resulta en un DataFrame monthly_sales donde cada fila representa un mes y el valor es
 la suma de las ventas de ese mes.
"""
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

import pandas as pd

# Paso 1: Carga el archivo CSV en un DataFrame
df = pd.read_csv('datos.csv')

# Paso 2: Convierte el tipo de datos de la columna "Fecha" a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Paso 3: Convierte el tipo de datos de la columna "Cantidad" a tipo entero
df['Cantidad'] = df['Cantidad'].astype(int)

# Paso 4: Establece la columna "Fecha" como índice del DataFrame
df.set_index('Fecha', inplace=True)

# Paso 5: Filtra el DataFrame para mostrar solo las ventas realizadas a partir del 2023-01-04
resultado_1 = df[df.index >= '2023-01-04']

# Guarda el resultado como CSV
resultado_1.to_csv('resultado_1.csv')

# Paso 6: Filtra el DataFrame para mostrar solo las ventas de un producto específico, por ejemplo, "Producto A"
resultado_2 = df[df['Producto'] == 'Producto A']

# Guarda el resultado como CSV
resultado_2.to_csv('resultado_2.csv')

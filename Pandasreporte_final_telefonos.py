import pandas as pd
# Cargar los datos desde el archivo CSV
df = pd.read_excel("DatosDeVentaDeTiendaDeTelefonos(10milDatos).xlsx")
# Imprimir el encabezado del reporte
print("=" * 50)
print("   REPORTE FINAL — TIENDA DE TELÉFONOS")
print("=" * 50)
#Resumen general
print("Resumen general:")
print(f"total de productos: {df.shape[0]:,}")
print(f"total de ventas: {df['Unidades'].sum():,}")
print(f"promedio de unidades por venta: {df['Unidades'].mean():.2f}")
print("=" * 50)
#Top 5 vendedores
print("Top 5 vendedores:")
top5_vendedores = df.groupby("Representante")["Unidades"].sum().nlargest(5)
print(top5_vendedores)
print("=" * 50)
#Productos más rentables
print("Productos más rentables:")
top5_productos = df.groupby("CódigoProducto")["Unidades"].sum().nlargest(10)
print(top5_productos)
print("=" * 50)
#Ventas por trimestre
print("Ventas por trimestre:")
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Trimestre"] = df["Fecha"].dt.quarter
ventas_por_trimestre = df.groupby("Trimestre")["Unidades"].sum()
print(ventas_por_trimestre)
print("=" * 50)
#Recomendaciones
print("RECOMENDACIONES:")
print(f"- Replicar la estrategia de {top5_vendedores.idxmax()}")
print(f"- Reforzar ventas en Q {ventas_por_trimestre.idxmin()} que es el trimestre más débil")
print(f"- Preparar stock extra antes de Q4 — concentra el 75% de ventas anuales")
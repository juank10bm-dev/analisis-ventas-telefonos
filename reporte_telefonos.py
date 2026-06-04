import pandas as pd

# Cargar datos
df = pd.read_excel("DatosDeVentaDeTiendaDeTelefonos(10milDatos).xlsx")

print("=" * 50)
print("   REPORTE DE VENTAS — TIENDA DE TELÉFONOS")
print("=" * 50)

# 1. Resumen general
print("\n📊 RESUMEN GENERAL:")
print(f"Total registros:        {df.shape[0]:,}")
print(f"Total unidades vendidas:{df['Unidades'].sum():,}")
print(f"Promedio por venta:     {df['Unidades'].mean():.2f}")

# 2. Mejor vendedor
print("\n🏆 TOP 5 VENDEDORES:")
top5_vendedores = df.groupby("Representante")["Unidades"].sum().nlargest(5)
print(top5_vendedores)

# 3. Productos más vendidos
print("\n📦 TOP 5 PRODUCTOS:")
top5_productos = df.groupby("CódigoProducto")["Unidades"].sum().nlargest(5)
print(top5_productos)

# 4. Ventas por mes
print("\n📅 VENTAS POR MES:")
df["Mes"] = df["Fecha"].dt.month
ventas_mes = df.groupby("Mes")["Unidades"].sum()
print(ventas_mes)

# 5. Ventas por año
print("\n📈 VENTAS POR AÑO:")
df["Año"] = df["Fecha"].dt.year
ventas_año = df.groupby("Año")["Unidades"].sum()
print(ventas_año)

print("\n" + "=" * 50)
print("   FIN DEL REPORTE")
print("=" * 50)


resumen = {
    "Métrica": ["Total registros", "Total unidades", "Promedio por venta"],
    "Valor": [df.shape[0], df["Unidades"].sum(), round(df["Unidades"].mean(), 2)]
}

df_resumen = pd.DataFrame(resumen)
df_resumen.to_excel("reporte_telefonos.xlsx", index=False)
print("Reporte exportado exitosamente!")
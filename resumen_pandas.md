📚 Resumen Pandas — Nivel 1 y 2
🔵 NIVEL 1 — Los fundamentos
pythonimport pandas as pd

# ─────────────────────────────────────
# CARGAR DATOS
# ─────────────────────────────────────

# Cargar CSV
df = pd.read_csv("archivo.csv")

# Cargar Excel
df = pd.read_excel("archivo.xlsx")

# ─────────────────────────────────────
# EXPLORAR — siempre lo primero
# ─────────────────────────────────────

df.shape        # cuántas filas y columnas → (10000, 4)
df.columns      # nombres de columnas
df.dtypes       # tipo de cada columna
df.head(5)      # primeras 5 filas
df.tail(5)      # últimas 5 filas
df.describe()   # estadísticas automáticas
df.info()       # resumen general

# ─────────────────────────────────────
# ACCEDER A DATOS
# ─────────────────────────────────────

df["columna"]                    # una columna
df[["col1", "col2"]]             # varias columnas
df.iloc[0]                       # primera fila por posición
df.loc[0]                        # primera fila por índice

# ─────────────────────────────────────
# ESTADÍSTICAS BÁSICAS
# ─────────────────────────────────────

df["col"].sum()     # suma total
df["col"].mean()    # promedio
df["col"].max()     # valor máximo
df["col"].min()     # valor mínimo
df["col"].count()   # contar valores

# ─────────────────────────────────────
# FILTRAR DATOS — como el if en Python
# ─────────────────────────────────────

df[df["precio"] > 80]              # mayor que
df[df["categoria"] == "Ropa"]      # igual a
df[df["stock"] < 30]               # menor que

# Filtro con dos condiciones
df[(df["precio"] > 80) & (df["stock"] > 20)]   # Y
df[(df["precio"] > 80) | (df["stock"] > 20)]   # O

# ─────────────────────────────────────
# CREAR COLUMNAS NUEVAS
# ─────────────────────────────────────

df["ingreso"] = df["precio"] * df["ventas"]
df["igv"]     = df["precio"] * 0.18
df["total"]   = df["precio"] + df["igv"]

# ─────────────────────────────────────
# EXPORTAR RESULTADOS
# ─────────────────────────────────────

df.to_excel("reporte.xlsx", index=False)
df.to_csv("reporte.csv", index=False)

🟠 NIVEL 2 — Análisis profundo
python# ─────────────────────────────────────
# ORDENAR DATOS
# ─────────────────────────────────────

# De mayor a menor
df.sort_values("ventas", ascending=False)

# De menor a mayor
df.sort_values("ventas", ascending=True)

# ─────────────────────────────────────
# CONTAR REPETIDOS
# ─────────────────────────────────────

# Cuántas veces aparece cada valor
df["producto"].value_counts()

# ─────────────────────────────────────
# DATOS VACÍOS — limpieza de datos
# ─────────────────────────────────────

df.isnull().sum()          # contar vacíos por columna
df.isnull().sum() / len(df) * 100  # porcentaje de vacíos
df.dropna()                # eliminar filas con vacíos
df.fillna(0)               # rellenar vacíos con 0
df.fillna("Sin datos")     # rellenar vacíos con texto

# ─────────────────────────────────────
# AGRUPAR DATOS — el más importante
# ─────────────────────────────────────

# Agrupar por una columna
df.groupby("categoria")["ventas"].sum()
df.groupby("categoria")["ventas"].mean()
df.groupby("categoria")["ventas"].max()

# Agrupar por dos columnas
df.groupby(["año", "categoria"])["ventas"].sum()

# Top 5 — los más grandes
df.groupby("vendedor")["ventas"].sum().nlargest(5)

# El campeón — solo el primero
df.groupby("vendedor")["ventas"].sum().idxmax()

# ─────────────────────────────────────
# UNIR TABLAS — como BUSCARV en Excel
# ─────────────────────────────────────

# Une dos tablas por una columna común
df_completo = df_ventas.merge(
    df_productos,
    on="CódigoProducto",  # columna común
    how="left"            # mantiene todas las filas de la izquierda
)

# ─────────────────────────────────────
# TABLA DINÁMICA — como Excel
# ─────────────────────────────────────

tabla = pd.pivot_table(
    df,
    values="Unidades",        # qué calcular
    index="Mes",              # filas
    columns="NombreProducto", # columnas
    aggfunc="sum",            # cómo calcular
    fill_value=0              # reemplaza NaN con 0
)

# ─────────────────────────────────────
# ANÁLISIS TEMPORAL — por fechas
# ─────────────────────────────────────

# Extraer partes de la fecha
df["Año"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month
df["Dia"] = df["Fecha"].dt.day

# Agrupar por período de tiempo
df_tiempo = df.set_index("Fecha")
df_tiempo["Unidades"].resample("ME").sum()  # por mes
df_tiempo["Unidades"].resample("QE").sum()  # por trimestre
df_tiempo["Unidades"].resample("YE").sum()  # por año

🎯 El patrón que siempre se repite
python# Todo análisis en Pandas sigue este patrón:

# 1. OBTENER
df.groupby("columna")

# 2. TRANSFORMAR
["columna"].sum().sort_values(ascending=False)

# 3. MOSTRAR
print()

💎 Los 7 secretos del analista
1. Antes de tocar datos → EDA primero
   shape, dtypes, isnull, describe

2. Datos sucios → siempre hay NaN
   isnull(), fillna(), dropna()

3. groupby es tu mejor amigo
   Agrupa, suma, ordena → insights

4. merge une mundos
   Dos tablas separadas → una completa

5. pivot_table cuenta la historia
   Filas × Columnas = Patrón oculto

6. resample revela temporadas
   El negocio tiene ciclos → encuéntralos

7. El insight vale más que el dato
   Dato: "iPhone vendió más"
   Insight: "iPhone es el 34% del negocio"
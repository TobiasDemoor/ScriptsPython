import pandas as pd
import matplotlib.pyplot as plt
import datetime

# https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv

def group(df: pd.DataFrame, param: list = ["fecha_apertura"]) -> pd.Series:
    return df.filter(param).groupby(param).size()

def movingAverage(series: pd.Series, period: int = 7) -> pd.Series:
    return series.rolling(period).sum() / period

def plotSeries(series: pd.Series, **kwargs):
    series.plot(**kwargs)
    plt.show()


datos: pd.DataFrame = pd.read_csv("./covid/Covid19Casos.csv")
confirmados: pd.DataFrame = datos.query('clasificacion_resumen == "Confirmado"')
# print(f"Cantidad de positivos: {len(confirmados)}")

# confirmDiarios = group(confirmados)
# ma7ConfirmDiarios = movingAverage(confirmDiarios)
# totalesConfirm = confirmDiarios.cumsum()

# plotSeries(confirmDiarios.plot())
# plotSeries(ma7ConfirmDiarios.plot())
# plotSeries(totalesConfirm.plot())


# fecha_internacion != None clasificacion contiene "/No activo/" -> ultima_actualizacion - fecha_internacion
# fecha_internacion != None fallecido == "SI" -> fecha_fallecimiento - fecha_internacion
def diasInternado(row: pd.Series, date_format: str = '%Y-%m-%d') -> int:
    parse_date = lambda string : datetime.datetime.strptime(string, date_format)
    datei = parse_date(row['fecha_internacion'])
    if row.fallecido == "SI":
        datef = parse_date(row['fecha_fallecimiento'])
    else:
        datef = parse_date(row['ultima_actualizacion'])
    return (datef - datei).days


internados = confirmados.dropna(subset=['fecha_internacion'])
internados = internados.query(
    'residencia_provincia_nombre != "SIN ESPECIFICAR" and ' +
    '(fallecido == "SI" or clasificacion.str.contains("No activo"))',
    engine='python'
)

internados["dias_internado"] = internados.apply(diasInternado, axis=1)

# limpiar los datos
internados = internados.filter(['dias_internado', 'residencia_provincia_nombre'])
internados = internados[internados.dias_internado > 0]

grouped = internados.groupby('residencia_provincia_nomjbre')
fig, ax = plt.subplots()
grouped.boxplot(subplots=False, rot=45, ax = ax)
fig.subplots_adjust(bottom=0.25, left=0.05, right=0.95, top=1.0)
plt.show()
    
import sys
sys.exit(0)

# as_index = False
# financiamiento = group(confirmados, ["fecha_apertura", "origen_financiamiento"])
# plotSeries(financiamiento)
# print(financiamiento)

fallecidos = confirmados.query('fallecido == "SI"')
# print(f"Cantidad de fallecidos: {len(fallecidos)}")

fallDiarios = group(fallecidos)
# ma7FallDiarios = movingAverage(fallDiarios)
# totalesFall = fallDiarios.cumsum()

# plotSeries(fallDiarios)
# plotSeries(ma7FallDiarios)
# plotSeries(totalesFall)


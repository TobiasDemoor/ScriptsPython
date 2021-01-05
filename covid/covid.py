import pandas as pd
import matplotlib.pyplot as plt
import datetime
from scipy.stats import norm
from math import sqrt

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
fallecidos: pd.DataFrame = confirmados.query('fallecido == "SI"')

def diasDeInternacionPorProvincia():
    global fallecidos

    def diasInternado(row: pd.Series, date_format: str = '%Y-%m-%d') -> int:
        parse_date = lambda string : datetime.datetime.strptime(string, date_format)
        datei = parse_date(row['fecha_internacion'])
        datef = parse_date(row['fecha_fallecimiento'])
        return (datef - datei).days

    internados = fallecidos.dropna(subset=['fecha_internacion'])
    internados = internados.query('carga_provincia_nombre != "SIN ESPECIFICAR"')

    internados["dias_internado"] = internados.apply(diasInternado, axis=1)

    # limpiar los datos
    internados = internados.filter(['dias_internado', 'carga_provincia_nombre'])
    internados = internados[internados.dias_internado > 0]

    grouped = internados.groupby('carga_provincia_nombre')
    fig, ax = plt.subplots()
    grouped.boxplot(subplots=False, rot=45, ax = ax, whis=[5, 95])
    fig.subplots_adjust(bottom=0.25, left=0.05, right=0.95, top=1.0)
    plt.show()


def tasaMortalidadPorProvincia():
    global confirmados, fallecidos

    confirmados_provincia = group(confirmados, ['carga_provincia_nombre'])
    fallecidos_provincia = group(fallecidos, ['carga_provincia_nombre'])
    tasa_provincia = fallecidos_provincia/confirmados_provincia

    # calculo el sigma de confianza
    sigma_provincia = []
    alpha = 0.95
    z_alpha = norm.ppf(alpha)
    for index, tasa in enumerate(tasa_provincia):
        sigma_provincia.append(z_alpha * sqrt((tasa*(1-tasa))/confirmados_provincia[index]))

    fig, ax = plt.subplots()
    tasa_provincia.plot(kind="bar", ax=ax, label="Muertes/Confirmados")
    plt.plot(tasa_provincia.index, tasa_provincia.count()*[tasa_provincia.mean()], 'g--', label="Media")
    plt.plot(tasa_provincia.index, sigma_provincia, 'k-.', label="Confianza")
    plt.legend()
    plt.show()

# print(f"Cantidad de positivos: {len(confirmados)}")

# confirmDiarios = group(confirmados)
# ma7ConfirmDiarios = movingAverage(confirmDiarios)
# totalesConfirm = confirmDiarios.cumsum()

# plotSeries(ma7ConfirmDiarios.plot())
# plotSeries(confirmDiarios.plot())
# plotSeries(totalesConfirm.plot())

# print(f"Cantidad de fallecidos: {len(fallecidos)}")

# fallDiarios = group(fallecidos)
# ma7FallDiarios = movingAverage(fallDiarios)
# totalesFall = fallDiarios.cumsum()

# plotSeries(fallDiarios)
# plotSeries(ma7FallDiarios)
# plotSeries(totalesFall)

# tasaMortalidadPorProvincia()
# diasDeInternacionPorProvincia()
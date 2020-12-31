import pandas as pd
import matplotlib.pyplot as plt

# https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv

def diarios(df: pd.DataFrame, param: list = ["fecha_apertura"]) -> pd.Series:
    return df.filter(param).groupby(param).size()

def movingAverage(series: pd.Series, period: int = 7) -> pd.Series:
    return series.rolling(period).sum() / period

def plotSeries(series: pd.Series):
    plt.axes(series.plot())
    plt.show()

df = pd.read_csv("./covid/Covid19Casos.csv")
confirmados = df.query('clasificacion_resumen == "Confirmado"')
# print(f"Cantidad de positivos: {len(confirmados)}")

# confirmDiarios = diarios(confirmados)
# ma7ConfirmDiarios = movingAverage(confirmDiarios)
# totalesConfirm = confirmDiarios.cumsum()

# plotSeries(confirmDiarios.plot())
# plotSeries(ma7ConfirmDiarios.plot())
# plotSeries(totalesConfirm.plot())

fallecidos = confirmados.query('fallecido == "SI"')
# print(f"Cantidad de fallecidos: {len(fallecidos)}")

fallDiarios = diarios(fallecidos)
ma7FallDiarios = movingAverage(fallDiarios)
totalesFall = fallDiarios.cumsum()

# plotSeries(fallDiarios)
# plotSeries(ma7FallDiarios)
# plotSeries(totalesFall)


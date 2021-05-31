import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

#Zad1
'''
data = pd.read_excel("imiona.xlsx")
df = pd.DataFrame(data)
'''

#Zad2
'''
data = pd.read_excel("imiona.xlsx")
df = pd.DataFrame(data)

#a
print(df[df['Liczba'] >1000])
#b
print(df[df['Imie'] == 'WIKTOR'])
#c
print(df.agg({'Liczba':['sum']}))
#d
print(df[(df.Rok < 2006)].agg({'Liczba': ['sum']}))
#e
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
#f
print(df.sort_values('Liczba',ascending=False).groupby(['Rok','Plec']).nth(0))
#g
print("M")
print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'),ascending=False).iloc[0])
print("K")
print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'),ascending=False).iloc[0])
'''

#Zad3
'''
data = pd.read_csv("zamowienia.csv", header=0, sep=';', decimal=".")
df = pd.DataFrame(data)

#a
print(df['Sprzedawca'].unique())
#b
print(df.sort_values(by='Utarg',ascending=False)['Utarg'][0:5])
#c
print(df.groupby(['Sprzedawca']).size())
#d
print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))
#e
print(df[((df['Kraj'] == 'Polska')) & (df['Data zamowienia'] <= '2005-12-31') & (df['Data zamowienia'] >= '2005-01-01')].agg({'Utarg':['sum']}))
#f
print(df[((df['Data zamowienia'].str[:4] =='2004'))]['Utarg'].mean())
#g
rok2004 = df[((df['Data zamowienia'].str[:4] =='2004'))]
rok2005 = df[((df['Data zamowienia'].str[:4] =='2005'))]
rok2004.to_csv("zamowienia_2004.csv",sep=';',index=False)
rok2005.to_csv("zamowienia_2005.csv",sep=';',index=False)
'''
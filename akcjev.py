from alpha_vantage.timeseries import TimeSeries

from matplotlib import pyplot as plt

KEY='******************'
ts=TimeSeries(key=KEY,)
nazwa=input("podaj jaki indeks chcesz sprawdzić np(#AAPL S&P500 DAX)")
data=ts.get_daily(nazwa)



info=data[1]
data=data[0]


lista_wynikow=[]
najwiecej=[]
najmniej=[]
lista_x=[]
for dana in data.values():
    najwiecej.append(float(dana['2. high']))
    najmniej.append(float(dana['3. low']))
    lista_wynikow.append((float(dana['2. high'])+float(dana['3. low']))/2)
    
for dana in data.keys():
    lista_x.append(dana)

lista_x.reverse()
lista_wynikow.reverse()
najmniej.reverse()
najwiecej.reverse()
suwaczek=40
plt.plot(lista_x,lista_wynikow,label='srednia',color='b')
plt.plot(lista_x[::len(lista_x)//suwaczek],najwiecej[::len(lista_x)//suwaczek],label='najwiecej',color='g',marker='o', linestyle='')
plt.plot(lista_x[::len(lista_x)//suwaczek],najmniej[::len(lista_x)//suwaczek],label='najmniej',color='r',marker='o', linestyle='')
plt.xlabel('Data')
plt.ylabel('średnia USD')


plt.grid()

plt.xticks([lista_x[0], lista_x[-1]]+lista_x[::len(lista_x)//4])
plt.tight_layout()
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.axis('tight')




plt.show()

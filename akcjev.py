from alpha_vantage.timeseries import TimeSeries

from matplotlib import pyplot as plt

KEY='S7L9K8TV3GBQIQ7I'
ts=TimeSeries(key=KEY,)

data=ts.get_daily('Nasdaq')

info=data[1]
data=data[0]

szuk='2023-07-25'
#AAPL S&P500 DAX
#szuk=input("podaj z jakiej daty wyszukujesz?")

# for x in data.values():
#     print(x)

# for jed,dwa in data[szuk].items():
#     print(jed+':'+dwa)

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
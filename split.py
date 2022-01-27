#“.split” per separare le stringhe su uno specifico carattere
mia_stringa = 'Ciao, come va?' 
print('stringa:{}'.format(mia_stringa))
lista_elementi = mia_stringa.split(',')
print('stringa tagliata: {}'.format(lista_elementi))

#conversione di una stringa a valore numerico (floating point)
mia_stringa = '5.5' 
mio_numero = float(mia_stringa)
print (mio_numero)

x=mio_numero+6
print('stampa somma numero:{}'.format(x))

#aggiungere elemento a lista
mia_lista = [1,2,3] 
mia_lista.append(4)
print(mia_lista)
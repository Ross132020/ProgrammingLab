#print (my_file.read() [0:50]) #slicing
#slice dal carttere 0 incluso al 50esimo escluso
#stampo solo 50 cartteri per non riempire il foglio e avere un'idea di cosa ci sia dentro
#stampo quindi i primi 50caratteri
#contenuto=my_file.read()
    #if len(contenuto) > 50: 
        #print(contenuto[0:50] + '...') #2stringhe
#else: print(contenuto)

# print(my_file.readline())   #spaziatura in aggiunta


# Inizializzo una lista vuota per salvare i valori 
#values = []
# Apro e leggo il file, linea per linea 
#myfile=open('shampoo_sales.csv','r') 
#print(myfile.readline())
   #r sta per read
   #per scrivere si mette rw
#for line in myfile:
    #elements=line.split(',')
# Faccio lo split di ogni riga sulla virgola 
    
# Se NON sto processando l’intestazione... 
    #if elements[0] != 'Date': # Setto la data e il valore 
        #date = elements[0] 
        #value = elements[1]
        # Aggiungo alla lista dei valori questo valore 
        #values.append(value)

#print('lista:{}'.format(myfile))





def somma_valori(myfile):
    values=[]
    for line in myfile:
        elements=line.split(',')
        if (elements[0] != 'Date'):
            numero=elements[1]
            values.append(float(numero))
    myfile.close()
    return(sum(values))
myfileshampoo=open('shampoo_sales.csv','r')
risultato=somma_valori(myfileshampoo)
print('risultato somma: {}'.format(risultato))


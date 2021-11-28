my_file = open('shampoo_sales.csv', 'r')
    print (my_file.read() [0:50]) #slicing
    #slice dal carttere 0 incluso al 50esimo escluso

        #r sta per read
        #per scrivere si mette rw
    contenuto= my_file.read()
#stampo solo 50 cartteri per non riempire il foglio e avere un'idea di cosa ci sia dentro
#stampo quindi i primi 50caratteri
    if len(contenuto) > 50: 
        print(contenuto[0:50] + '...') #2stringhe
else: print(contenuto)

# print(my_file.readline())   #spaziatura in aggiunta

#faccio riga per riga
      for line in my_file:
   #Faccio lo split di ogni riga sulla virgola
      elements = line.split(',')
   #Faccio lo split di ogni riga sulla virgola

# Se NON sto processando l’intestazione...
if elements[0] != 'Date':
# Setto la data e il valore
        date = elements[0]
        value = elements[1]
# Aggiungo alla lista dei valori questo valore
values.append(float(value))   

my_file.close()
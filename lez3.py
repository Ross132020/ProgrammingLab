myfile= open('shampoo_sales.csv','r')
#print(myfile.read()[0:62])

print(myfile.readline())#spaziatura
print(myfile.readline())
print(myfile.readline()) #vale come spaziatura
print(myfile.readline())
print(myfile.readline()) #riga4

for line in myfile:
    print(line) #ciclo che legge il file riga per riga ma in un colpo, cioè senza stare a scrivere di stampare riga per riga




#scrivo sul file 
myfile1=open('shampoo_sales.csv','w')
myfile1.write('ciao world!')

print (myfile1.read)
#leggo il file modificato con il testo
myfile.close()

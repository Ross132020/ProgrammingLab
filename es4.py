# esercizio slide 4 Lab.

class CSVFile():

    def __init__(self,date,sales):
        self.date = date
        self.sales = sales

    def get_data(self,lista):

        for i in range(0,len(lista)):
            concatenate =str(lista(data)) + str(lista(sales)) #oppure si utilizza la funzione __str__(self,......) indicandone il ritorno con return

try:
    esercizio = CSVFile.get_data(open('shampoo_sales.csv','r'))
    print('soluzione: {}'.format(esercizio))
except Exception as e:
    print('errore rilevato: "{}"'.format(e))
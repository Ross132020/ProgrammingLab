#modello base, oggetto model generico
class Model()
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
      
    def predict (self,data):
        #si poteva scrivere pass e avere un metodo vuoto, ma è preferibile avvisare nel caso si sbagli a prendere oggetto
        raise NotImplementedError('Metodo non implementato')

#creo una sottoclasse, il mio modello che estende la classe Model
class IncrementModel(Model)
    def predict(self,data): 
      #calcolo slide degli incrementi file lezione8
      # questa fx deve tornare 65
        #data può essere per esempio una lista di valori, es 50, 52, 60
        for item in data:
            #Logica per la predizione
            n=len(data)
            #n dev'essere maggiore di 0
            if n>0:
                print('"n">0, si può continuare')
            else
                print('Error: n<0!!')

        prediction=
        return prediction

dati=[50,52,60]
prova=IncrementModel(dati)
print(prova)
#modello base
class Model()
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
      
    def predict (self,data):
        raise NotImplementedError('Metodo non implementato')

#creo una sottoclasse
class IncrementModel(Model)
    def predict(self,data):
        for item in data:
            #Logica per la predizione

        prediction=
        return prediction
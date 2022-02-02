import random

class Person():
  pass
person=Person() #istanzia la classe, crea una nuova istanza di persona
person1=Person()
print(person)
print(person1) #la stampa delle 2 istanze è diversa(locazione di memoria)
#definire +persone, istanziare + volte una classe
#l'oggetto viene rappresentato in stringa, quindi uso __str__, x stampare no robaccia

#Per cambiare come viene stampato un oggetto devo implementare la fx __str__
class Persona():
    def __init__(self, name, surname):
    #serie di parametri che vengono poi assegnati a qualcosa(me stesso, self)non definito finchè sta roba non viene istanziata
        self.name=name
        self.surname=surname
    #posso quindi accedere a queste variabili da fuori richiamandole, es person=Person('mario','rossi')
    def __str__(self):
        return '{}{}'.format(self.name, self.surname)
    def say_myname(self):
        print('My name is {}'.format(self.name))

class Worker(Persona):
    def __str__(self):
        return 'I am {}'.format(self.name)
    def say_myname(self):
        num=random.randint(0,2)
        if num==0:
            print('{} is a farmer'.format(self.name))
        elif num==1:
            print('{} is a football player'.format(self.name))
        elif num==2:
            print('{} is a business man/woman'.format(self.name))
    def original_say_myname(self):
        super().say_myname() #con il super() riporta il metodo della classe genitrice, ossia my name is...

person2=Persona('Mattia ','Carli')
print('person 2 is {}'.format(person2))
person2.say_myname()

persona3=Persona('Paride ','Stanley')
print('person 3 is {}'.format(persona3))
persona3.say_myname()

persona3=Worker('Paride ','Stanley')
persona3.say_myname()   
persona3.original_say_myname()  
print(persona3)  


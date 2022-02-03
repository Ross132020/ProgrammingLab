import random
#importo modulo per numeri randomici

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'Name: {}, age: {}'.format(self.name,self.age)
    def say_hi(self):
        #generare numero randomico
        random_number= random.randint(0, 3)
        if random_number ==0:
            print('{} with age {}, hi!'.format(self.name,self.age))
        elif random_number ==1:
            print('{} says hello!'.format(self.name))
        elif random_number ==2:
            print('{} says ciao!'.format(self.name))
        elif random_number == 3:
            print('{} says mandi!'.format(self.name))

#prova programma
person = Person('Marco', '15')
print('person 0 = {}'.format(person))
person.say_hi()


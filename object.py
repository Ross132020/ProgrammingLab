class Person():

  def __init__ (self, name, surname):
    # Set name and surname
    self.name = name
    self.surname = surname
    #il primo parametro è sempre self

    def __str__(self):
      return 'Person"{} {}""'
  
person= Person ('Mario', 'Rossi')
print (person)



class Student(Person):

  def __str__ (self):
    return 'Student "{}{}"'.format(self.name, self.surname)

class Professor(Person);
    def __str__(self):
      return 'Prof."{}{}"'.format(self.name, self.surname)

    def say_hi(self):
      print
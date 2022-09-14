from re import A


class People:
    all_people = []
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age
        People.all_people.append(self)
    
    def get_informasi(self):
        print(f"nama saya {self.name}, tinggi badan saya {self.height}, umur saya {self.age}")

class Animal:
    def __init__(self,name,species):
        self.a = name
        self.b = species
    
    def get_info(self):
        print(f"nama hewan {self.a}, species {self.b}")

        

patrick = People("Patrick",170,20)
gracia = People("Gracia",160,20)
willy = People("Willy",170,19)
Jupee = Animal("Jupee","hamster")


# kalo ini pake list all_people
for individual in People.all_people:
    print(f"nama {individual.name}, tinggi badan {individual.height}, umur {individual.age}")


patrick.get_informasi()
# bisa juga pake cara ini, hasilnya sama saja
People.get_informasi(gracia)
People.get_informasi(willy)

Jupee.get_info()


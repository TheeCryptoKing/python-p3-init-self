#!/usr/bin/env python3


# _init_ to intialize a new object 
# name of object = ClassName() to make an instance 
# callin init is us rewrting it always there for every class by default




class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

fido = Dog("fido")
print(fido.name)
print(fido.breed)

    # def get_adopted(self, owner_name):
    #     self.owner = owner_name

# fido = Dog("Dog")
# fido.get_adopted("Sophie")
# fido.owner






# class Dog:
#     pass
# fido = Dog()
# fido.breed = "Dalmation"
# def _init_(self, name):
#     print(f"{name} is born!")
# def showing_self(self):
#     return self
    
# fido = Dog("Fido")
# fido.showing_self()
# #fido is fido.showing_self() this refers  refers to the instance
# #self in python = this in Javascript




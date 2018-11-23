# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Person():
    def __init__(self,name,age):
       self.name = name
       self.age = age
       
    def __str__(self):
        return("%r is %r years old"%(self.name,self.age))

    def health(self):
        self.condition=input('%s Do you have any medical condition:'%self.name)
        return self.condition
    @classmethod
    def greeting(cls):
        return 'Welcome'
    @staticmethod
    def title():
        return 'Hi this a medical report of a family'


A = Person('Abdulvahab',36)
ha=A.health()
B = Person('Musarratbanu',34)
hb=B.health()
C = Person('Fatema',9)
hc=C.health()
D = Person('Abdulrehman',6)
hd=D.health()

print(A.title())    
print(B.greeting())
print(f'''{A}
          {ha}
          {B}
          {hb}
          {C}
          {hc}
          {D}
          {hd}''')

def activity(self):
    Person[A] 
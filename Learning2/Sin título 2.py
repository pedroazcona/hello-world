import os

class Complex:
    def __init__(self, realpart, imagpart):
       self.r = realpart
       self.i = imagpart

    def SumComplex(self,y):
        self.r=self.r+y.r
        self.i=self.i+y.i
        return self

        
class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name=name
        self.tricks = []   
    def add_trick(self, trick):
        self.tricks.append(trick)

def reverse(data):
    for index in range(len(data)-1, -1,-1):
        yield data[index]

def reverse2(data):
    pata =[]
    for index in range(len(data)):
        pata.append(data[index])
    pata.reverse()
    yield pata    

def reverse3(data):
    pata =data.reverse()
    yield pata

for i in range(50):
    print (i, os.strerror(i))




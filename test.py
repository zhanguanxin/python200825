from __future__ import print_function

import pickle
import os

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if 0 < age < 100:
            self.__age = age

    def dispaly(self):
        print("Person('%s', %d)" % (self.__name, self.__age))

    def __str__(self):
        return "Person('%s', %d)" % (self.__name, self.__age)


p = Person('zhanguanxin', 35)

p.dispaly()

p.age = 45

print(str(p.age))
p.dispaly()

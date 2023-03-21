# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:42:47 2023

@author: jocelyn
"""
## ejercicios para practicar
class Duck:
    sound='Quack!'
    walking='Walks like a duck'
    
    def quack(self):
        print(self.sound)
        
    def walk(self):
        print(self.walking)
        
def main():
    donald=Duck()
    donald.quack()
    
if __name__ == '__main__':main()

'''
SECOND EXCERCISE
'''

## ejercicios para practicar
class Robot:
    def introduce_self(self):
        print('My name is ' + self.name)

r1 = Robot()
r1.name = 'Robotin'
r1.color= 'Red'
r1.weight=30
   
r2 = Robot()
r2.name = 'Rob'
r2.color = 'Blue'
r2.weight = 40
    
r1.introduce_self()
r2.introduce_self()

'''
Better looking classes + making interacting classes
'''
#to fix it we will use a constructor so we avoid writing too much text for each variable and avoid errors
# constructor __init__
class Robot:
    def __init__(self,n,c,w):
        self.name=n
        self.color=c
        self.weight=w
         
    def introduce_self(self):    
        print('My name is ' + self.name)

r1 = Robot('Robotin','Red',30)
r2 = Robot('Robbie','Orange',40)
  
r1.introduce_self()
r2.introduce_self()

'''
second class
'''
class Person:
    def __init__(self,n,p,i):
        self.name=n
        self.personality=p
        self.is_sitting=i
    
    def sit_down(self):
        self.is_sitting =True
        
    def stand_up(self):
        self.is_sitting =False
 
p1= Person("Cindy", "Calm", False)
p2=Person('Jocelyn','Happy',True)
       
#p1 owns r2, set robot attribute to p1
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
#the result is: "My name is Robbie"


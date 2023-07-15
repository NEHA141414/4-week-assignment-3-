#!/usr/bin/env python
# coding: utf-8

# Q-1 Create a vehicle class with an init method having instance variable as name_of_vehicle,max_speed and average_of_vehicle.

# In[3]:


class vehicle:
    def __init__ (self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle
        
v1=vehicle("Thar",150,700000)
print(v1.name_of_vehicle)
print(v1.max_speed)
print(v1.average_of_vehicle)


# Q-2 Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
#  Create a method named seating_capacity which  takes capacity as an argument and returns the name of the vehicle and its seating capacity.

# In[4]:


class vehicle:
    def __init__ (self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle
        
    def return_func(self):
        return self.name_of_vehicle,self.max_speed,self.average_of_vehicle
class child(vehicle):
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle,capacity):
        super() .__init__(name_of_vehicle,max_speed,average_of_vehicle)
        self.capacity=capacity
        
    def func1(slef):
        print(self.name_of_vehicle,self.capacity)
        x=child("Lamborghini",350,720,90)
        x.func1()


# Q-3 What is multiple inheritance ? Write a python code to demonstrate multiple inheritance.

# In[5]:


'''
 When a class is derived  from more than one base class it is called multiple inheritance .The derived class inherits all the features of the base case.'''

class class1:
    def me(self):
        print("In class1")

class class2(class1):
    def me(self):
        print("In class2")
        
class class3(class1):
    def me(self):
        print("In class3")
        
class class4(class2,class3):
    pass
obj=class4()
obj.me()


# Q-4 What are getter and setter in python ? create a class and create a getter and setter method in this class.

# In[10]:


'''
Getter: A method that allow you to access an attribute in a given class.
Setter: A method that allows you to set or mutate the values of an attribute in a class.'''


class person:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x
  
raj = person()
  
# setting the age using setter
raj.set_age(21)
  
# retrieving age using getter
print(raj.get_age())
  
print(raj._age)


# Q-5 What is method overriding in python ? Write a python code to demonstrate  method overriding.

# In[12]:


#  Method Overriding : When you have two methods with the same name that each perform different tasks.


# method overriding
  
  
# Defining parent class
class Parent():
      
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Child(Parent):
      
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
          
    # Child's show method
    def show(self):
        print(self.value)
          
          
# Driver's code
obj1 = Parent()
obj2 = Child()
  
obj1.show()
obj2.show()


# In[ ]:





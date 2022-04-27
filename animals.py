from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes
    age = None
    name = None

    #Constructors
    def __init__(self, name, age):
        self.value = "Animal"
        self.name = name
        self.age = age

    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        print("I am sleeping")

    def type(self):
        print(self.value)

class Mammal(Animal):
    #Attributes
    
    

    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        print("Live Birth")

    def sleep(self):
        print("I am sleeping now")

    def type(self):
        print(self.value)

class Cat(Mammal):
    #Attributes


    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Cat"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return("I eat mice")
     

class Bat(Mammal):
    #Attributes

    flying = "True"
    
    Fur = "Yes"

    Location = "BatCave"

    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Bat"

    #Methods
    def type(self):
        print(self.value)

    def eat(self):
        print("Insects")
        
    def reproduce(self):
        print("I lay eggs")
    
    def sleep(self):
        print("I sleep upsidedown")

class Bird(Animal):
    #Attributes

    Beak = "true"

    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Bird"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    def reproduce(self):
        print("I lay eggs")
    
    def sleep(self):
        print("I am sleeping now")

    def type(self):
         print(self.value)   

class Penguin(Bird):
    #Attributes

    flying = False

    Location = "Antarctica"


    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Penguin"

    #Methods
    def type(self):
        print(self.value)
    def eat(self):
        print("I eat fish")
    def reproduce(self):
        print("I lay eggs")

class Pigeon(Bird):
    #Attributes

    flying = "true"

    location = "London"

    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Pigeon"

    #Methods
    def type(self):
        print(self.value)
    def eat(self):
        print("I eat bread")
    def reproduce(self):
        print("I lay eggs")

class Seagull(Bird):
    #Attributes

    wings = "Long wings"

    flying = True

    location = "Brighton"

    #Constructors
    def __init__(self,name,age):
        super().__init__(name,age)
        self.value = "Seagull"

    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat litter"

    def speed(self):
        return "I can fly up to 28mph"

    def weight(self):
        return "I can weigh as much as 3.8 pounds"
    

    
    

from animals import Animal, Cat, Bat, Pigeon, Penguin, Seagull


AnimalList = []
message = "Thank you for visiting our vet!"

for i in [Cat("Mittens the Cat", 3),Bat("Bruce the bat", 7),Pigeon("Chirpie the Pigeon", 6),Penguin("Chilly the Penguin", 1),Seagull("Rio the Seagull", 1)]:
    AnimalList.append(i)

userInput = int(input("Welcome to our Vet! He look after a range of animals!\nTo view the animals in our vet, enter [1], to exit the program, enter [0]: "))



if userInput == 0:
    print(message) 

elif userInput == 1:
    for animal in AnimalList:
         print (animal.name+ ", " + str(animal.age) + " years old ")


    print(message)


else:
    print("Re-run the program")
    exit



class Animals:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def info(self):
        print(f"Hi there. My name is {self.name} and I am a", type(self).__name__)

    def eating(self):
        print(f"I eat {self.eat} everyday")

    def sleeping(self):
        print(f"I need to sleep for {self.sleep} hours to feel good")

    def isanimal(self):
        if isinstance(self, Animals):
            print("It is obvious - I am an animal")
        else:
            print("I don't now how, but it seems like I am not an animal")


#===================DOG CLASS====================


class Dog(Animals):
    def __init__(self, name, eat, sleep, voice):
        super().__init__(name, eat, sleep)
        self.voice = voice

    def speak(self):
        print(f"All I can say is '{self.voice}'")

    def friend(self):
        print("I will be your best friend forever!")


dog = Dog("Patron", "bones", 10, "Bark")
dog.info()
dog.eating()
dog.sleeping()
dog.speak()
dog.friend()
dog.isanimal()
print()


#===================CAT CLASS====================#


class Cat(Animals):
    def __init__(self, name, eat, sleep, voice):
        super().__init__(name, eat, sleep)
        self.voice = voice

    def speak(self):
        print(f"All I can say is '{self.voice}'")

    def roomie(self):
        print(f"That guy {dog.name} can't stop barking. I just want to sleep!")


cat = Cat("Sonya", "fish", 16, "Meow")
cat.info()
cat.eating()
cat.sleeping()
cat.speak()
cat.roomie()
cat.isanimal()
print()


#===================FROG CLASS====================#


class Frog(Animals):
    def __init__(self, name, eat, sleep, voice):
        super().__init__(name, eat, sleep)
        self.voice = voice

    def speak(self):
        print(f"All I can say is '{self.voice}'")

    def wednesday(self):
        print("It's Wednesday, my dudes!")


frog = Frog("Jimmy", "flies", 5, "Quack")
frog.info()
frog.eating()
frog.sleeping()
frog.speak()
frog.wednesday()
frog.isanimal()
print()


#===================SNAKE CLASS====================#


class Snake(Animals):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def wish(self):
        print("I wish to be an actress")


snake = Snake("Nagini", "muggles", 6)
snake.info()
snake.eating()
snake.sleeping()
snake.wish()
snake.isanimal()
print()


#===================CRAB CLASS====================#


class Crab(Animals):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def dollar(self):
        print("Money? Who said money?")


crab = Crab("Mr. Crabs", "burgers", 8)
crab.info()
crab.eating()
crab.sleeping()
crab.dollar()
crab.isanimal()
print()


#===================HUMAN CLASS====================#


class Human:
    def __init__(self, eat, sleep, study, work):
        self.eat = eat
        self.sleep = sleep
        self.study = study
        self.work = work

    def eating(self):
        print(f"{self.eat} is my favourite food")

    def sleeping(self):
        print(f"{self.sleep} hours of sleep is definitely not enough")

    def studying(self):
        print(f"Learning {self.study} is hard, but I am trying and I'll do it!")

    def working(self):
        print(f"I work for {self.work} now")

    def wish(self):
        print("Can't wait till my new keyboard comes ^_^")


#===================CENTAUR CLASS====================#


class Centaur(Animals, Human):
    def __init__(self, name, eat, sleep, study, work):
        Human.__init__(self, eat, sleep, study, work)
        Animals.__init__(self, name, eat, sleep)

    def shoes(self):
        print("Did anybody see my sneakers? Lost them again!")


centaur = Centaur("Alberto", "pizza", 8, "Python", "taxi driver")

centaur.info()
centaur.eating()
centaur.sleeping()
centaur.studying()
centaur.working()
centaur.wish()
centaur.isanimal()

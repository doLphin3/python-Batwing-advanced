from abc import abstractmethod, ABC
from random import randint


class Client(ABC):
    def __init__(self, name, age, availability_of_money, have_own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.have_own_home = have_own_home

    @abstractmethod
    def info(self):
        raise NotImplementedError('This method is not realised')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('This method is not realised')

    @abstractmethod
    def buy_a_house(self, house):
        raise NotImplementedError('This method is not realised')


class Person(Client):
    def __init__(self, name, age, availability_of_money, have_own_home):
        super().__init__(name, age, availability_of_money, have_own_home)

    def info(self):
        print(f"The person's name is {self.name}")
        print(f"Age: {self.age}")
        print(f"Amount of money: ${self.availability_of_money}")
        print(f"{self.name} has his own house: {self.have_own_home}")

    def make_money(self):
        self.availability_of_money += randint(1, 10) * 10000
        print(f"{self.name} earned some money. He has ${self.availability_of_money} total now.")

    def buy_a_house(self, house):
        self.house = house
        if realtor.steal_money():
            print("The deal is canceled.")
        elif self.age < 18:
            print(f"{self.name}'s age is under 18. He can not buy a house yet.")
        elif self.have_own_home:
            print(f"{self.name} has his own house already.")
        elif house.cost >= self.availability_of_money:
            print("The deal is canceled. Not enough money.")
        else:
            realtor.give_a_discount(house)
            self.availability_of_money -= house.cost - (house.cost * realtor.discount / 100)
            self.have_own_home = True
            realtor.houses.remove(house)
            print(f"Deal! {self.name} just bought his own house!")


class House:
    def __init__(self, name, area, cost, discount):       # discount in percents
        self.name = name
        self.area = area
        self.cost = cost
        self.discount = discount

    def apply_discount(self):
        return self.discount

    def __str__(self):
        return self.name

    def house_info(self):
        print(f"> {self.name}")
        print(f" - Area: {self.area}m^2")
        print(f" - Cost: ${self.cost}")
        print(f" - Available discount from owner: {self.discount}%")
        
    
class SmallHouse(House):
    def __init__(self, name, area, cost, discount):       # discount in percents
        super().__init__(name, area, cost, discount)

    def house_info(self):
        print(f"> {self.name}")
        print(f" - Area: {self.area}m^2")
        if self.area < 40:
            print("The area is more than 40m^2. This house is not so small :/")
        print(f" - Cost: ${self.cost}")
        print(f" - Available discount from owner: {self.discount}%")


class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses, discount):       # discount in percents
        self.name = name
        self.houses = houses
        self.discount = discount

    def info_about_houses(self):
        print(f"Realtor {self.name} has {len(self.houses)} houses:")
        for house in range(0, len(self.houses)):
            House.house_info(self.houses[house])

    def give_a_discount(self, house):   # the realtor can not give a bigger discount than the owner
        if self.discount > House.apply_discount(house):
            self.discount = House.apply_discount(house)
        print(f"{house}: Available discount from realtor is {self.discount}%")
        return self.discount

    def steal_money(self):
        if randint(1, 10) == 1:
            print("Realtor have stolen the money!")
        else:
            return False


house1 = House("House 1", 40, 50000, 10)
house2 = House("House 2", 70, 80000, 5)
small_house = SmallHouse("Small house", 50, 30000, 2)
small_house.house_info()

realtor = Realtor("Matt", [house1, house2,  small_house], 7)
realtor.info_about_houses()

person = Person("Jack", 54, 100000, False)
person.info()
person.make_money()
print()
person.buy_a_house(house2)
print()
person.info()
print()
realtor.info_about_houses()

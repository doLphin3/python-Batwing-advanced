class Person:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def info_str(self):
        print(f"Name: {self.name}")
        print(f"Last name: {self.last_name}")
        print(f"Phone number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"E-Mail: {self.email}")
        print(f"Birthday: {self.birthday}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")

    def info_list(self):
        print(list(self.__dict__.values()))


person = Person('John', 'Cena', '+10506050504', 'Drohobych', 'cena@meta.ua', '13.12.85', '27', 'male')
person.info_str()
print()
person.info_list()

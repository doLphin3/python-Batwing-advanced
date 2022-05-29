# COMPOSITION ========================================
class Person:
    def __init__(self):
        left_arm = Arm("Left arm")
        right_arm = Arm("Right arm")
        self.arm1 = left_arm.side
        self.arm2 = right_arm.side

    def drums(self):
        print(f"I use my {self.arm1} to play a snare and my {self.arm2} to play a hi-hat.")


class Arm:
    def __init__(self, side):
        self.side = side


person = Person()
person.drums()
print()


# AGGREGATION ========================================

class CellPhone:
    def __init__(self, model, type_of_display):
        self.type_of_display = type_of_display
        self.model = model

    def info(self):
        print(f"{self.model} has a display type {self.type_of_display}")


class Screen:
    def __init__(self, display):
        self.display = display


super_amoled = Screen("Super Amoled")
oled = Screen("OLED")
ips = Screen("IPS")

samsung = CellPhone("Samsung", super_amoled.display)
samsung.info()
xiaomi = CellPhone("Xiaomi", oled.display)
xiaomi.info()
iphone = CellPhone("iPhone", ips.display)
iphone.info()

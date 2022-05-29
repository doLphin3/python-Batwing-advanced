from abc import abstractmethod, ABC

# Interface


class Laptop:
    @abstractmethod
    def screen(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def webcam(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def ports(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError('This method was not implemented')

##


class HPLaptop(Laptop):
    def screen(self):
        print('15.6" display')

    def keyboard(self):
        print('Ukrainian')

    def touchpad(self):
        print('Touchpad +')

    def webcam(self):
        print('1.3 MP')

    def ports(self):
        print('USB, HDMI, Ethernet, VGA')

    def dynamics(self):
        print('2 dynamics')


hp = HPLaptop()
hp.screen()
hp.keyboard()
hp.touchpad()
hp.webcam()
hp.ports()
hp.dynamics()

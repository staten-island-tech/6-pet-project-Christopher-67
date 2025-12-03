class Pet:
    def __init__(self, name):
        self.name = name
        self.__happiness = 5
        self.__hunger = 5
        self.__energy = 5

    def get_happiness(self):
        return self.__happiness

    def get_hunger(self):
        return self.__hunger

    def get_energy(self):
        return self.__energy
    
    def _change_happiness(self, amount):
        self.__happiness = max(0, min(10, self.__happiness + amount))

    def _change_hunger(self, amount):
        self.__hunger = max(0, min(10, self.__hunger + amount))

    def _change_energy(self, amount):
        self.__energy = max(0, min(10, self.__energy + amount))

    def feed(self):
        print(f"{self.name} is eat")
        self._change_hunger(-2)
        self._change_happiness(1)
    
    def play(self):
        print(f"{self.name} is playing")
        self._change_happiness(3)
        self._change_energy(-2)
        self._change_hunger(1)
    
    def sleep(self):
        print(f"{self.name} is sleeping")
        self._change_energy(2)
        self._change_hunger(1)
    
    def status(self):
        return {
            "happiness": self.get_happiness(),
            "hunger": self.get_hunger(),
            "energy": self.get_energy()
        }
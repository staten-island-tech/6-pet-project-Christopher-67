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
        self.__happiness = self.__happiness + amount
        if self.__happiness > 10:
            self.__happiness = 10
        else:
            if self.__happiness < 0:
                self.__happiness = 0

    def _change_hunger(self, amount):
        self.__hunger = self.__hunger + amount
        if self.__hunger > 10:
            self.__hunger = 10
        else:
            if self.__hunger < 0:
                self.__hunger = 0

    def _change_energy(self, amount):
        self.__energy = self.__energy + amount
        if self.__energy > 10:
            self.__energy = 10
        else:
            if self.__energy < 0:
                self.__energy = 0

    def feed(self):
        print(f"feeding {self.name}")
        if self.__hunger < 4:
            print(self.name, "kinda eating")
            self._change_hunger(-2)
        elif self.__hunger < 7:
            print(self.name, "eating")
            self._change_hunger(-3)
            self._change_happiness(1)
        else:
            print(self.name, "eatingx2")
            self._change_hunger(-4)
            self._change_happiness(2)
        
        if self.__hunger < 2:
            print("cant eat much")
        else:
            if self.__hunger > 7:
                print("eat a lot")

    def rest(self):
        print(f"{self.name} resting")
        if self.__energy >= 6:
            print(self.name, "sleep a bit")
            self._change_energy(2)
            self._change_hunger(1)
        elif self.__energy >= 3:
            print(self.name, "sleep")
            self._change_energy(3)
            self._change_hunger(1)
        else:
            print(self.name, "sleep")
            self._change_energy(4)
            self._change_hunger(1)

        if self.__energy < 3:
            print("sleep more")
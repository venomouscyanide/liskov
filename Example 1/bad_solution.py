# bad way to solve the bird_ex.py


class Bird:
    def __init__(self):
        self._lat = 0
        self._long = 0
        self._altitude = 0

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def set_lat(self, lat: float):
        self._lat = lat

    @property
    def long(self):
        return self._long

    @long.setter
    def set_long(self, long: float):
        self._long = long

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def set_altitude(self, altitude):
        self._altitude = altitude

    def draw(self):
        # A complex non sense function to record a flight pattern
        if isinstance(self, Penguin):
            return self._lat * pow(self._long, 4)
        else:
            return self._lat * pow(self._long, 4) + self._altitude


class Penguin(Bird):
    def set_altitude(self, altitude):
        raise NotImplementedError('Does not have altitude')


def main():
    crow = Bird()
    crow.set_lat = 234.2
    crow.set_long = 24.2
    crow.set_altitude = 100
    print(crow.draw())
    # now comes a penguin
    penguin = Penguin()
    penguin.set_lat = 10
    penguin.set_long = 100
    # penguin.set_altitude(0)
    # When the app is run, all the flying patterns look wrong because the Penguin objects ignore the setAltitude method
    print(penguin.draw())


if __name__ == '__main__':
    main()

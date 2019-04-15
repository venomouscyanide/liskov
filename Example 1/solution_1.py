# band aid solution


class Bird:
    def __init__(self):
        self._lat = 0
        self._long = 0
        self._altitude = 0
        # extra flag to differentiate birds who can and can't fly
        self._is_flightless = False

    @property
    def is_flightless(self):
        return self._is_flightless

    @is_flightless.setter
    def set_is_flightless(self, is_flightless):
        self._is_flightless = is_flightless

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

    def check_if_flightless(self):
        if self._is_flightless:
            return True
        else:
            return False

    def draw(self):
        # A complex non sense function to record a flight pattern
        if self.check_if_flightless():
            return self._lat * pow(self._long, 4)
        else:
            return self._lat * pow(self._long, 4) + self._altitude


def main():
    crow = Bird()
    crow.set_lat = 234.2
    crow.set_long = 24.2
    crow.set_altitude = 100
    crow.set_is_flightless = False
    print(crow.draw())
    # now comes a penguin
    penguin = Bird()
    penguin.set_lat = 10
    penguin.set_long = 100
    penguin.set_is_flightless = True
    print(penguin.draw())


if __name__ == '__main__':
    main()

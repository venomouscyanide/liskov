# a proper solution


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


class FlightfulBird(Bird):
    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def set_altitude(self, altitude):
        self._altitude = altitude

    def draw(self):
        # A complex non sense function to record a flight pattern
        return self._lat * pow(self._long, 4) + self._altitude


class FlightlessBird(Bird):
    def draw(self):
        return self._lat * pow(self._long, 4)


def main():
    crow = FlightfulBird()
    crow.set_lat = 234.2
    crow.set_long = 24.2
    crow.set_altitude = 100
    print(crow.draw())
    # now comes a penguin
    penguin = FlightlessBird()
    penguin.set_lat = 10
    penguin.set_long = 100
    print(penguin.draw())


if __name__ == '__main__':
    main()

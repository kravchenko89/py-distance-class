class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, value: float):
        return Distance(self.km * value)

    def __truediv__(self, value: float):
        return Distance(round(self.km / value, 1))

    def __lt__(self, other):
        return self.km < other.km

    def __le__(self, other):
        return self.km <= other.km

    def __gt__(self, other):
        return self.km > other.km

    def __ge__(self, other):
        return self.km >= other.km

    def __eq__(self, other):
        return self.km == other.km

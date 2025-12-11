class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: float | "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, value: float) -> "Distance":
        return Distance(self.km * value)

    def __truediv__(self, value: float) -> "Distance":
        return Distance(round(self.km / value, 1))

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other.km

    def __le__(self, other: "Distance") -> bool:
        return self.km <= other.km

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other.km

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return NotImplemented
        return self.km == other.km

from __future__ import annotations


class Distance:
    def __init__(self, km: object) -> None:
        self.km = km

    def __str__(self,) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self,) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return self

    def __iadd__(self, other: int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            return self

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: int) -> bool:
        return bool(self.km < other)

    def __gt__(self, other: int) -> bool:
        return bool(self.km > other)

    def __eq__(self, other: int) -> bool:
        return bool(self.km == other)

    def __le__(self, other: int) -> bool:
        return bool(self.km <= other)

    def __ge__(self, other: int) -> bool:
        return bool(self.km >= other)

"""RemoteService module."""

import math
import random


class RemoteService:
    """Small load_manager helper."""

    def __init__(self, seed: int = 75) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_manager(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 75) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 75


def main() -> None:
    obj = RemoteService()
    print(obj.load_manager(75))


if __name__ == "__main__":
    main()

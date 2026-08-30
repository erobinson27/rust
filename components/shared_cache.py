"""SimpleSession module."""

import math
import random


class SimpleSession:
    """Small render_session helper."""

    def __init__(self, seed: int = 54) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_session(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 54) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 54


def main() -> None:
    obj = SimpleSession()
    print(obj.render_session(54))


if __name__ == "__main__":
    main()

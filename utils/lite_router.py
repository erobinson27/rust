"""RemoteCache module."""

import math
import random


class RemoteCache:
    """Small render_handler helper."""

    def __init__(self, seed: int = 71) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_handler(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 71) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 71


def main() -> None:
    obj = RemoteCache()
    print(obj.render_handler(71))


if __name__ == "__main__":
    main()

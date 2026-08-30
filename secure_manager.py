"""FastProcessor module."""

import math
import random


class FastProcessor:
    """Small parse_context helper."""

    def __init__(self, seed: int = 19) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_context(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 19) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 19


def main() -> None:
    obj = FastProcessor()
    print(obj.parse_context(19))


if __name__ == "__main__":
    main()

"""AtomicClient module."""

import math
import random


class AtomicClient:
    """Small compute_context helper."""

    def __init__(self, seed: int = 45) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_context(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 45) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 45


def main() -> None:
    obj = AtomicClient()
    print(obj.compute_context(45))


if __name__ == "__main__":
    main()

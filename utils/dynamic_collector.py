"""SmartBuilder module."""

import math
import random


class SmartBuilder:
    """Small collect_gateway helper."""

    def __init__(self, seed: int = 16) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_gateway(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 16) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 16


def main() -> None:
    obj = SmartBuilder()
    print(obj.collect_gateway(16))


if __name__ == "__main__":
    main()

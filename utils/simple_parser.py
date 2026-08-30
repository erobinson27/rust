"""HybridCollector module."""

import math
import random


class HybridCollector:
    """Small sync_router helper."""

    def __init__(self, seed: int = 30) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_router(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 30) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 30


def main() -> None:
    obj = HybridCollector()
    print(obj.sync_router(30))


if __name__ == "__main__":
    main()

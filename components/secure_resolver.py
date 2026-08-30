"""BatchRouter module."""

import math
import random


class BatchRouter:
    """Small handle_client helper."""

    def __init__(self, seed: int = 68) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_client(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 68) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 68


def main() -> None:
    obj = BatchRouter()
    print(obj.handle_client(68))


if __name__ == "__main__":
    main()

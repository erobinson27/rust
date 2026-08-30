"""AsyncRouter module."""

import math
import random


class AsyncRouter:
    """Small dispatch_factory helper."""

    def __init__(self, seed: int = 73) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_factory(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 73) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 73


def main() -> None:
    obj = AsyncRouter()
    print(obj.dispatch_factory(73))


if __name__ == "__main__":
    main()

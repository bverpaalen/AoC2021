from __future__ import annotations


class Lanternfish:

    def __init__(self, timer: int) -> None:
        self.b_timer = timer

    def tick(self) -> Lanternfish or None:
        self.b_timer -= 1

        if self.b_timer < 0:
            self.b_timer = 6
            return self.birth()
        return None

    @staticmethod
    def birth() -> Lanternfish:
        return Lanternfish(8)

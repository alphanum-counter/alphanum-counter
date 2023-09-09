from __future__ import annotations
class IncorrectFormatException(Exception):
    def __init__(self, value) -> None:
        self.message = f"Incorrect value: {value}"
        super().__init__(self.message)


class UnsupportedException(Exception):
    def __init__(self, message: str) -> None:
        self.message = f"Unsupported: {message}"
        super().__init__(self.message)

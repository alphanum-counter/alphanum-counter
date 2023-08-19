import re
from typing import Tuple


class IncorrectFormatException(Exception):
    def __init__(self, value) -> None:
        self.message = f"Incorrect value: {value}"
        super().__init__()

class AlphanumCounter(object):
    
    def __init__(self, start=None, alpha_pos=1, max_num=1000):
        """
        :param alpha_num: number of alphabet positions in the beginning.
        :param max_num: maximum count until numbers are increased.
        """
        assert isinstance(alpha_pos, int)
        self._alpha_pos = alpha_pos
        assert isinstance(max_num, int)
        self._max_num=max_num
        self._set_start(start)
        super(AlphanumCounter, self).__init__()

    def _set_start(self, start) -> str:
        if not start:
            self._current = f"A{self._format_num('0')}"
        else:
            alpha, num = self._split_alpha_num(start)
            self._current = f"{alpha}{self._format_num(num)}"

    def current(self) -> str:
        return self._current

    def _increase_counter(self):
        alpha, num = self._split_alpha_num(self._current)
        if int(num) == self._max_num:
            alpha = self._next_alpha(alpha)
            num = self._reset_num(num=num)
        else:
            next_num = int(num) + 1
            num = self._format_num(f"{next_num}")

        self._current = f"{alpha}{num}"

    def _split_alpha_num(self, num: str) -> Tuple:
        if not isinstance(num, str):
            raise IncorrectFormatException(num)

        splits = re.findall(r"[^\W\d_]+|\d+", num)

        if len(splits) != 2:
            raise IncorrectFormatException(num)
        elif not splits[0].isalpha():
            raise IncorrectFormatException(num)
        else:
            try:
                int(splits[1])
            except Exception:
                raise IncorrectFormatException(num)

        return splits[0], splits[1]

    def _next_alpha(self, alpha):
        return chr((ord(alpha.upper())+1 - 65) % 26 + 65)        

    def _reset_num(self, num) -> str:
        return self._format_num("1")

    def _format_num(self, num) -> str:
        length = len(num)
        max_count_len = len(str(self._max_num))
        return f"{(max_count_len - length)* '0'}{num}"

    def next(self) -> str:
        self._increase_counter()
        return self._current
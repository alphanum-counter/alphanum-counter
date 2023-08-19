from itertools import count
import pytest
from alphanum_counter.counter import AlphanumCounter

def test_counter_1():
    counter = AlphanumCounter()
    assert counter.current() == 'A0000'
    assert counter.next() == 'A0001'


def test_counter_2():
    counter = AlphanumCounter(start='A100', max_num=100)
    assert counter.current() == 'A100'
    assert counter.next() == 'B001'

import pytest
from alphanum_counter.counter import AlphanumCounter
from alphanum_counter.exceptions import UnsupportedException, IncorrectFormatException

def test_counter_1():
    counter = AlphanumCounter()
    assert counter.current() == 'A0000'
    assert counter.next() == 'A0001'


def test_counter_2():
    counter = AlphanumCounter(start='A100', max_num=100)
    assert counter.current() == 'A100'
    assert counter.next() == 'B001'


def test_counter_3():
    with pytest.raises(IncorrectFormatException):
        AlphanumCounter(start='1B2')

    with pytest.raises(IncorrectFormatException):
        AlphanumCounter(start='B')

    with pytest.raises(IncorrectFormatException):
        AlphanumCounter(start=1)


def test_counter_4():
    with pytest.raises(UnsupportedException):
        AlphanumCounter(alpha_pos=2)
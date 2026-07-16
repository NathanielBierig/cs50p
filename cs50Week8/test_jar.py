import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_capacity():
    jar = Jar(20)
    assert jar.capacity == 20

    with pytest.raises(ValueError):
        Jar(-1)


def test_deposit():
    jar = Jar()

    jar.deposit(5)

    assert jar.size == 5


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)

    assert jar.size == 3


def test_deposit_overflow():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw_too_many():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_str():
    jar = Jar()

    jar.deposit(3)

    assert str(jar) == "\nCookies: 🍪🍪🍪 (3/12)"


import pytest

from jar import Jar


def test_init():
    jar=Jar(3)
    assert jar.capacity==3
    jar=Jar()
    assert jar.capacity==12
    

    test_str()
    test_deposit()
    test_withdraw()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size==4
    jar.deposit(6)
    jar.size==10

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert str(jar) == "🍪"
    assert jar.capacity==12
    jar.deposit(9)
    assert jar.size==10
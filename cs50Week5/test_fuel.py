import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from cs50Week3 import fuel
import pytest


def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("99/100") == 99


def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"


def test_convert_exceptions():
    with pytest.raises(ValueError):
        fuel.convert("3/2")

    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
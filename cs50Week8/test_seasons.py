from datetime import date, timedelta
from seasons import calc_minutes
import pytest

def test_birthday():
    today = date.today()

    # Reference dates
    reference_today = date(today.year, 7, 16)
    reference_birthday = date(2005, 6, 10)

    # Shift birthday by however many days today differs from July 16
    offset = today - reference_today
    test_birthday = reference_birthday + offset

    assert calc_minutes(test_birthday.isoformat()) == ("Eleven million, ninety-six thousand, six hundred forty minutes")


def test_today():
    today = date.today().isoformat()
    assert calc_minutes(today) == "Zero minutes"


def test_one_year():
    today = date.today()
    last_year = date(today.year - 1, today.month, today.day).isoformat()

    assert calc_minutes(last_year) == "Five hundred twenty-five thousand, six hundred minutes"


def test_invalid():
    with pytest.raises(ValueError):
        calc_minutes("hello")

    with pytest.raises(ValueError):
        calc_minutes("01-01-2000")

    with pytest.raises(ValueError):
        calc_minutes("2000/01/01")

    
    future = (date.today() + timedelta(days=1)).isoformat()

    with pytest.raises(ValueError):
        calc_minutes(future)
import pytest
from working import convert


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:15 PM to 12:30 AM") == "12:15 to 00:30"
    assert convert("1 PM to 2 AM") == "13:00 to 02:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("cat")

    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 PM to 13 AM")
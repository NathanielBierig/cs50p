import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from cs50Week2 import plates

def test_valid():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("HELLO") == True
def test_length():
    #2-6
    assert plates.is_valid("A") == False
    assert plates.is_valid("ABCDEFG") == False
def test_start():
    #cant start with num, no num in between, must start 2 letters
    assert plates.is_valid("1ABC") == False
    assert plates.is_valid("A1BC") == False
def test_numbers():
    #first num cant be 0
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS50") == True
def test_punctuation():
    #no special chars or spaces
    assert plates.is_valid("PI.3") == False
    assert plates.is_valid("CS 50") == False
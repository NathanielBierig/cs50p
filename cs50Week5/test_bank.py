import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from cs50Week1 import bank

def test_hello():
    assert bank.value("Hello") == 0
def test_h():
    assert bank.value("Hi") == 20
    assert bank.value("Hellooooooo") == 20
    assert bank.value("Hell naaahahaha") == 20
    assert bank.value("Hey") == 20
def test_other():
    assert bank.value("Whats up") == 100
    assert bank.value("What it do") == 100
    assert bank.value("Wazzzaaaap") == 100
    assert bank.value("*nods") == 100
    assert bank.value("Whats up") == 100
    assert bank.value("chgtyuytfghgy987") == 100
    assert bank.value("345678ihgfcvgbnm") == 100
    assert bank.value("bvbnbv drtyufx") == 100













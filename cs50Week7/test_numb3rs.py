from numb3rs import validate

def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("127.0.0.1") == True


def test_invalid():
    assert validate("256.0.0.1") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("abc") == False
    assert validate("1.2.3.256") == False
    assert validate("01.2.3.4") == False
    assert validate("1.2.3.-1") == False
    assert validate("1.2.3.a") == False
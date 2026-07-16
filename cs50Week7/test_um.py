from um import count


def test_single():
    assert count("um") == 1


def test_multiple():
    assert count("um, um, um") == 3


def test_case():
    assert count("Um uM UM") == 3


def test_words():
    assert count("yummy album umbrella") == 0


def test_mixed():
    assert count("Um, thanks, um... that was um!") == 3
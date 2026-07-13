import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from cs50Week2 import twttr
import string
import random
VOWELS = ["a","A", "e","E", "i", "I", "o", "O", "u", "U"]
def generate_random_string():
    characters = string.ascii_letters + string.digits
    
    # Randomly choose characters and merge them
    return ''.join(random.choices(characters, k=30))

# Example usage

def test_shorten():
    try:
        # hard coded (for project)
        assert twttr.shorten("Hello World") == "Hll Wrld"
        assert twttr.shorten("123abc") == "123bc"
        assert twttr.shorten("The blue parrot thoughtfully juggled several avocados while contemplating the meaning of time.") == "Th bl prrt thghtflly jggld svrl vcds whl cntmpltng th mnng f tm."
# general, optimal
        for x in range(10):
            result = twttr.shorten(generate_random_string())
            for vowel in VOWELS:
                assert vowel not in result
    
    except AssertionError:
        print("Fail)")
# def main():
#     test_shorten()

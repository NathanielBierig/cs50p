import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #tests 250-255,249-200,1xx,99-0
    rpattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    return bool(re.search(rpattern , ip))


if __name__ == "__main__":
    main()
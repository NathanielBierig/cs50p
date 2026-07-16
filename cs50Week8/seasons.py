from datetime import date
import inflect



def main():
    print(calc_minutes(input("Enter Birthday YYYY-MM-DD: ")))

def calc_minutes(bday):
    birthday = date.fromisoformat(bday)
    if birthday > date.today():
        raise ValueError
    difference = date.today() - birthday
    minutes = difference.days * 24 * 60
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize()+ " minutes"


if __name__ == "__main__":
    main()
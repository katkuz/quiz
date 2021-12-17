import re
from datetime import date
from tentamen.api import get_nobel_prizes
from tentamen.category import cat
from tentamen.print_strings import START_MESSAGE, WRONG_YEAR_MESSAGE, QUITING_MESSAGE, WRONG_CATEGORY_MESSAGE, WRONG_INPUT_MESSAGE


def main():
    print(START_MESSAGE)
    while True:
        user_input_sting = input(">").strip()
        check_for_quit(user_input_sting)
        if re.match(r"[0-9]{4}$", user_input_sting):
            if get_year(user_input_sting) == -1:
                continue
            print_nobel_prizes(get_nobel_prizes({"nobelPrizeYear": get_year(user_input_sting)}))
        else:
            try:
                year, category = user_input_sting.split()
                if get_year(year) == -1:
                    continue
                if category not in cat.keys():
                    print(WRONG_CATEGORY_MESSAGE)
                    continue
                print_nobel_prizes(get_nobel_prizes({"nobelPrizeYear": int(year), "nobelPrizeCategory": cat[category]}))
            except ValueError:
                print(WRONG_INPUT_MESSAGE)
            continue


def check_for_quit(user_input_sting):
    """Check input from user and quit program if user want it

        user_input_sting
            input string from user
        """
    if user_input_sting == 'Q' or user_input_sting == 'q':
        print(QUITING_MESSAGE)
        quit()


def print_nobel_prizes(res):
    """Print list of nobel prizes from response

        res
            response as json object with info about prizes and laureates for selected parameters
        """
    for prize in res["nobelPrizes"]:
        prize_money = prize["prizeAmount"]
        prize_todays_money = prize["prizeAmountAdjusted"]
        print(f"{prize['categoryFullName']['se']} prissumma {prize_money} SEK")
        print("Laureates:")
        for laureate in prize["laureates"]:
            print_laureate(laureate, prize_money, prize_todays_money)
        print("")


def print_laureate(laureate, prize_money, prize_todays_money):
    """Print one laureate on screen from json object.

        laureate
            json object with info about a laureate
        prize_money
            total prize historical
        prize_todays_money
            total prize with inflation to current date
        """
    portion_number = 0
    try:
        portion_string = laureate['portion']
        if '/' in portion_string:
            num, den = portion_string.split('/')
            portion_number = float(num) / float(den)
        else:
            portion_number = int(portion_string)
    except ValueError:
        pass
    if 'knownName' in laureate.keys():
        print(f"  {laureate['knownName']['en']}: ", end='')
    if 'orgName' in laureate.keys():
        print(f"  {laureate['orgName']['en']}: ", end='')
    if portion_number != 0:
        print(f"{int(portion_number * int(prize_money))} / {int(portion_number * int(prize_todays_money))} SEK", end='')
    print(f" {laureate['motivation']['en']}")


def get_year(year_string):
    """Try to get year from string return year as int. Return -1 if string is not a year between 1901 and current year.

        year_string
            string to parse
        """
    match = re.match(r"[0-9]{4}$", year_string)
    if not match:
        print(WRONG_YEAR_MESSAGE)
        return -1
    year = int(match.string)
    if year < 1901 or year > date.today().year:
        print(WRONG_YEAR_MESSAGE)
        return -1
    return year


if __name__ == '__main__':
    main()

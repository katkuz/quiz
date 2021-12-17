import re
from datetime import date
from tentamen.api import get_nobel_prizes
from tentamen.category import cat
from tentamen.print_strings import START_MESSAGE, WRONG_YEAR_MESSAGE, QUITING_MESSAGE, WRONG_CATEGORY_MESSAGE, WRONG_INPUT_MESSAGE


def main():
    print(START_MESSAGE)
    while True:
        thy_command = input(">").strip()
        check_for_quit(thy_command)
        if re.match(r"[0-9]{4}$", thy_command):
            if get_year(thy_command) == -1:
                continue
            print_nobel_prizes(get_nobel_prizes({"nobelPrizeYear": get_year(thy_command)}))
        else:
            try:
                a, b = thy_command.split()
                if get_year(a) == -1:
                    continue
                if b not in cat.keys():
                    print(WRONG_CATEGORY_MESSAGE)
                    continue
                print_nobel_prizes(get_nobel_prizes({"nobelPrizeYear": int(a), "nobelPrizeCategory": cat[b]}))
            except ValueError:
                print(WRONG_INPUT_MESSAGE)
            continue


def check_for_quit(thy_command):
    if thy_command == 'Q' or thy_command == 'q':
        print(QUITING_MESSAGE)
        quit()


def print_nobel_prizes(res):
    for p in res["nobelPrizes"]:
        money = p["prizeAmount"]
        today_money = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {money} SEK")
        print("Laureates:")
        for m in p["laureates"]:
            print_laureate(m, money, today_money, 0)
        print("")


def print_laureate(m, money, today_money, result):
    try:
        andel = m['portion']
        if '/' in andel:
            num, den = andel.split('/')
            result = float(num) / float(den)
        else:
            result = int(andel)
    except ValueError:
        pass
    if 'knownName' in m.keys():
        print(f"{m['knownName']['en']}: ", end='')
    if 'orgName' in m.keys():
        print(f"{m['orgName']['en']}: ", end='')
    if result != 0:
        print(f"{int(result * int(money))} / {int(result * int(today_money))} SEK", end='')
    print(f" {m['motivation']['en']}")


def get_year(a):
    match = re.match(r"[0-9]{4}$", a)
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
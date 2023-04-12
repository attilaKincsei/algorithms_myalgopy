# https://www.codewars.com/kata/total-amount-of-points/train/python


def points(games):
    total_points = 0
    for match in games:
        home, guest = match.split(sep=":")
        if int(home) > int(guest):
            total_points += 3
        elif int(home) == int(guest):
            total_points += 1
    return total_points


def main():
    points([""])


if __name__ == '__main__':
    main()

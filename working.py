import re
import sys


def main():
    s = input("Hours: ")
    print(convert(s))


def convert(s):
    match = re.match(
        r'^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$',
        s
    )

    if not match:
        raise ValueError

    hour1 = int(match.group(1))
    minute1 = int(match.group(2)) if match.group(2) else 0
    period1 = match.group(3)

    hour2 = int(match.group(4))
    minute2 = int(match.group(5)) if match.group(5) else 0
    period2 = match.group(6)
    if not (1 <= hour1 <= 12 and 1 <= hour2 <= 12):
        raise ValueError
    if not (0 <= minute1 <= 59 and 0 <= minute2 <= 59):
        raise ValueError
    if period1 == "AM":
        if hour1 == 12:
            hour1 = 0
    else:
        if hour1 != 12:
            hour1 += 12
    if period2 == "AM":
        if hour2 == 12:
            hour2 = 0
    else:
        if hour2 != 12:
            hour2 += 12
    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
if __name__ == "__main__":
    main()

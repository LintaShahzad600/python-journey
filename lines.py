import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    count = 0

    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.strip() == "":
                continue

            if line.lstrip().startswith("#"):
                continue

            count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")

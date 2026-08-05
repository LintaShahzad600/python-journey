import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as file1:
        next(file1)

        with open(sys.argv[2], "w") as file2:
            file2.write("first,last,house\n")

            for line in file1:
                line = line.strip()

                name, house = line.split('",')
                name = name.replace('"', '')

                last, first = name.split(",")

                file2.write(f"{first.strip()},{last},{house}\n")

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

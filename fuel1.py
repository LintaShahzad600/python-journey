while True:
    try:
        x, y = input("FRACTION: ").split("/")
        x = int(x)
        y = int(y)
        if x > y or y == 0 or x < 0:
            continue
        percent = round((x / y) * 100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except (ValueError, ZeroDivisionError):
        pass

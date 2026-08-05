import re
def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))
    
def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        parts = ip.split(".")
        for part in parts:
            if len(part) > 1 and part.startswith("0"):
                 return False
            part = int(part)
            if part < 0 or part > 255:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()

def main():
    print("Greeting: ")
    greeting=input(" ").strip().lower()
    print("$"+str(value(greeting)))
def value(greeting):
     greeting=greeting.lower()
     show =" "
     if greeting.startswith("hello"):
       show=0
     elif greeting.startswith("h"):
       show=20
     else:
       show=100
     return show
if __name__ == "__main__":
    main()

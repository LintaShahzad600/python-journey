def convert(a):
    return a.replace(":)","🙂").replace(":(","🙁")
text=input("Enter text")
print(convert(text))
def main():
    text=input()
    print(convert(text))
    main()

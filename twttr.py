
def main():
    text=input(" ")
    print(shorten(text))
def shorten(word):
    output=""
    for letter in word:
     if letter.lower() not in['a','e','o','i','u']:
      output=output+letter
    return output

if __name__ == "__main__":
 main()

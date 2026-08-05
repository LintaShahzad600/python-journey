text=input("Input:")
output=""
for letter in text:
  if letter.lower() not in['a','e','o','i','u']:
        output=output+letter
print("Output:",output)



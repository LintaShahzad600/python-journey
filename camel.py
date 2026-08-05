camel = input("CamelCase: ")
snake = ""
for c in camel:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c
print("snake-case:",snake)

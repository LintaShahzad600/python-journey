def dollars_to_float (d):
    return float(d.replace("$",""))
def per_to_float(p):
    return float(p.replace("%",""))/100
dollar=dollars_to_float(input("How much was the meal"))
percentage=per_to_float(input("What percentage would u like to tip"))
tip=dollar*percentage
print(f"Leave ${tip:.2f}")

def convert(time):
    nums=time.split(":")
    h=int(nums[0])
    m=int(nums[1])
    return h + m/60
def main():
    answer=input("What time is it?")
    t=convert(answer)
    if 7 <= t <= 8:
      print("breakfast time")
    elif 12 <= t <= 13:
      print("lunch time")
    elif 18<= t <= 19:
      print("dinner time")
if __name__=="__main__":
   main()


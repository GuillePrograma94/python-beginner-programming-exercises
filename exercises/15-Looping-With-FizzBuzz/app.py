def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for x in range(1,101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else: 
            print(x)


# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()

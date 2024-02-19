# your code goes here!
import time

def countdown(number):
    x = int(number)
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!!")

# countdown(10)


def countdown_with_sleep(number):
    x = int(number)
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
        time.sleep(1)

    print("CAN YOU BE MY VALENTINE!")

countdown_with_sleep(10)
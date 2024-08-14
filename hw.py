import random

ans = random.randint(1, 100)
tries = 0
win = False

while not win:
    guess = int(input("Guess the number between 1 and 100: "))
    triess += 1
    if guess < ans:
        print("Your guess was too low.")
    elif guess > ans:
        print("Your guess was too high.")
    else:
        win = True
        print(f"You guessed the number in {tries} tries.")


def calculate(start, end):
    num = 5.00
    num2 = 2.50
    stops = end - start
    total = num + (num2 * stops)
    return total

start = int(input("What number stop are you at? "))
end = int(input("What is the stop you want to go to? "))
fare = calculate(start, end)
print(f"The fare from Stop {start} to Stop {end} is ${fare}")

print("===Welcome to Secret Number Guessing Name===\n")
secret_number= 12
attempt_counts= 5
print("You have 5 attempts!")

num_range= ("It can be any number between 1-50")
print("HINT- The hints provided are according to weather celcius!")
number= int(input("Please enter your guess: "))

if number== range(40,51):
    print("Wrong Answer!")
    print("I am not that hot")
    attempt_counts -= 1
elif number== range(30,40):
    print("Wrong Answer")
    print("I am a cold number")
    attempt_counts -= 1
elif number== range(20,30):
    print("You are getting close")
    print("But remember, Its still warm for me..")
    attempt_counts -=1
elif number== range(10,12):
    print("Woah, very very close")
    print("Going on right track")
    attempt_counts-=1
elif number== range(13,20):
    print("Close!")
    attempt_counts -=1
elif number== range(1,10):
    print("You gotta go a little warmer")
elif number== 12:
    print("Well done")
    print("You guessed the answer correctly")
else:
    print("Invalid Number")

if attempt_counts ==0:
    print("Sorry you lost.")
    print("The number was 12.")
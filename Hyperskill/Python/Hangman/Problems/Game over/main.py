scores = input().split()
# put your python code here

mistakes = 0
score = 0
lives = 3

for s in scores:
    if s == "C":
        score += 1
    elif s == "I":
        mistakes += 1
        if mistakes >= lives:
            print("Game over")
            break

if mistakes < lives:
    print("You won")

print(score)

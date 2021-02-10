samples = int(input())

matches = []
for i in range(samples):
    matches.append(input().split(" "))

winners = []
for match in matches:
    if match[1] == "win":
        winners.append(match[0])

print(winners)
print(len(winners))

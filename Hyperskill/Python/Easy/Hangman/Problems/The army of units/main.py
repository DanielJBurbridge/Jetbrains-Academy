size = int(input())
message = ""
if size < 1:
    message = "no army"
elif size < 10:
    message = "few"
elif size < 50:
    message = "pack"
elif size < 500:
    message = "horde"
elif size < 1000:
    message = "swarm"
else:
    message = "legion"

print(message)

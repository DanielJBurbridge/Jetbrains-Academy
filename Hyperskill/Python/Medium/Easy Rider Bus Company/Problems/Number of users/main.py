# write your code here
import json

my_users = {}

with open('users.json') as f:
    my_users = json.load(f)

print(len(my_users['users']))

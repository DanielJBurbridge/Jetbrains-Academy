import json


colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
          "CMYK": ["cyan", "magenta", "yellow", "key color"],
          "RBG": ["red", "blue", "green"]}

# write your code here

with open('colors.json', 'w') as f:
    json.dump(colors, f)

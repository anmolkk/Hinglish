import json

with open("data.json","r") as file:
    data = json.load(file)

search = None

word = input("Enter Hinglish Word: ")
word = word.capitalize()
if word in data:
    search = data[word]
    print(search)
else:
    print("Error in Code")
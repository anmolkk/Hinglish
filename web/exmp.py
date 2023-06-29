import json

with open("static/web/data.json","r") as file:
    data = json.load(file)


def find_matching_keys(dictionary, value):
    matching_keys = []
    for key in dictionary:
        if value in key.capitalize():
            matching_keys.append(key)
        elif value.capitalize() in key:
            matching_keys.append(key)

    if not matching_keys == []:
        if len(matching_keys) == 1:
            return matching_keys[0]
        else:
            return matching_keys[0],matching_keys[1]
    else:
        return None

matching_keys = find_matching_keys(data, "agar")
print(matching_keys)
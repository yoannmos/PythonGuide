import json

data_dictionary = {
    "Members": {
        "Names": "Paul",
        "Age": 32
    }
}

print(data_dictionary)

with open("data_file.json", "w") as write_file:
    json.dump(data_dictionary, write_file)


# # data_dictionary["Paul"] = 32
# # data_dictionary["Jack"] = 28
# # data_dictionary["Nils"] = 54
# json_string = json.dumps(data_dictionary)
# print(json_string)

# filter = "JSON File (*.json)|*.json|All Files (*.*)|*.*||"
# filename = rs.SaveFileName("Save JSON file as", filter)

# # If the file name exists, write a JSON string into the file.
# if filename:
#     # Writing JSON data
#     with open(filename, 'w') as f:
#         json.dumps(data_dictionary)

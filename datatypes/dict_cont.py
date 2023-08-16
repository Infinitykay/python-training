oau_user = {
  'faculties': ["Theater", "Arts", "Science", "Law"],
  'names': ["Ola", "Ade", "Tolu", "Tade"],
  "location": "Ile Ife",
  "main_campus": True,
  # "main_campus": False,
}
# print(oau_user["names"])
# Add to the dictionary
oau_user["departments"] = [
  "Computer Science", "Pub Admin", "Drama", "Chemistry"
]
# print(oau_user)
oau_user["location"] = {"main_campus": "Ile Ife", "secondary_campus": "Moro"}

# print(oau_user["location"]["main_campus"])
# print(oau_user["faculties"][2])
# print(oau_user["names"][1:3])
# print(oau_user["departments"][1:3])

# dict methods
# empty_dict = oau_user.clear()
# print(oau_user['color'])
print(oau_user.get("color", "Key not in dictionary"))
# print("color" not in oau_user)
print(len(oau_user))
# print(empty_dict)
# print(oau_user)
# print(oau_user.items())
# print(oau_user.keys())
# print(oau_user.values())

oau_user['location'].pop("secondary_campus")
oau_user['names'].remove("Ade")
print(oau_user)
oau_user = {
  'faculties': ["Theater", "Arts", "Science", "Law"],
  'names': ["Ola", "Ade", "Tolu", "Tade"],
  "location": "Ile Ife",
  "main_campus": True,
  "secondary_campus": False,
}

oau_user1 ={
  'faculties': ["Tech", "Admin", "SocialScience", "Education"],
  'names': ["Daniel", "Samson", "King", "Sami"],
  "location": "Ondo",
  "main_campus": True,
  "secondary_campus": False,
  "hostel": ["Moremi", "Alumni", "Awo"]
}

oau_user.popitem()

oau_user1.update(facultyyyyy=["Science", "Arts"])
print(oau_user1)


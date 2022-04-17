from animal_shelter import AnimalShelter

username = "aacuser"
password = "Skywalker7"

testBuild = AnimalShelter(username, password)

new_data = [
    {"age_upon_outcome": "3 years",
     "animal_id": "GH7001",
     "animal_type": "Dog",
     "breed": "Grey hound",
     "color": "Black",
     "date_of_birth": "2019-06-02",
     "datetime": "2000-01-01 01:00:00",
     "monthyear": "2000-01-01T01:00:00",
     "name": "Whimper",
     "outcome_subtype": "SCRP",
     "outcome_type": "Transfer",
     "sex_upon_outcome": "Neutered Male",
     "location_lat": "25.0000",
     "location_long": "71.0000",
     "age_upon_outcome_in_weeks": "56.012"}
]

for x in new_data:
    testBuild.creation(x)

tester = testBuild.reading({"animal_id": "GH7001"})
for y in tester:
    print(y)
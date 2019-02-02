# ##Create 5 dictionaries which have list values

dict1 = {'State': 'Maharashtra', 'City': 'Pune', 'Best Places to Visit': ['Shanivarwada', "Pataleshwar", "Dagdusheth", "Tulshibag"]}
dict2 = {'State': 'Goa', 'Cty': 'North Goa', 'Best Places to Visit': ["panji", "Baga", "Calngut", "Meeramaar"]}
dict3 = {'State': 'Maharashtra', 'City': 'Pune', 'Best Hotel to Visit': ["PK Biryani", "Vaishali", "Jogeshwari", "Surves"]}
dict4 = {'State': 'GOA', 'City': 'North Goa', 'Best Hotel to Visit': ["RITZ", "DE Baga DECK", "DE Calangut DECK", "Pinkvilla"]}
dict5 = {'pune':["VEGMARATHA", "Pav Bhaji", "MASTANI", "MISALPAV"], 'GOA': ["Mahroom omlette", "Fish thali", "RAVA FRY-"]}

print("WHEN I ROME WITH MY FRIEND IN", dict1['City'],
      "I usually go with my friends to visit", dict1['Best Places to Visit'][1],
 "&", dict1['Best Places to Visit'][3]
      )

print("every year we go to", dict2['State'], "we use to stay at", dict2['Best Places to Visit'][2])

print("In", dict4['City'], "we love to go", dict4['Best Hotel to Visit'][0],
      "and", dict4['Best Hotel to Visit'][2], "Hotel"
      )

print("when you visit to", dict1['City'], "City dont forget to taste",
      dict5['pune'][2], "and", dict5['pune'][3]
      )

print("when you visit to", dict4['City'], "City dont forget to taste",
      dict5['GOA'][2], "and", dict5['GOA'][0]
      )

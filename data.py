# This was created by: Owen Pence
# First changes 


# This category is the protein options

salmon = {
     "calories": 1000,
    "category": "protein",
}
chicken = {
  "calories": 900,
  "category": "protein", 
}
milk = {
  "calories": 250,
  "category": "protein", 
}
turkey = {
  "calories": 171,
  "category": "protein",
}
blackbeans = {
  "calories": 341,
  "category": "protein",
}
beef = {
  "calories": 902,
  "category": "protein",
}
tuna = {
  "calories": 144,
  "category": "protein",
}
almonds = {
  "calories": 579,
  "category": "protein",
}
broccoli = {
  "calories": 62,
  "category": "protein",
}
pork = {
  "calories": 124,
  "category": "protein",
}



print(["protein"])

meal = []

meal.append(chicken["protein"])
meal.append(salmon["protein"])
meal.append(milk["protein"])
meal.append(turkey["protein"])
meal.append(blackbeans["protein"])
meal.append(beef["protein"])
meal.append(tuna["protein"])
meal.append(almonds["protein"])
meal.append(broccoli["protein"])

print(meal)

proteins = 0

for i in meal:
    print(i)
    if i == "protein":
        proteins += 1

print(proteins)
# Module 7: Fair Food Stands
# Emily Smith

# Starting with dictionaries to represent food stands
food_stands = {
    "Pronto Pups": "Corn Dogs",
    "Big Fat Bacon": "Bacon-on-a-Stick"
}

# Print the food stands
print("Food stands at the fair:")
for stand, food in food_stands.items():
    print(stand + ": " + food)

# Adding a new food stand
food_stands["Fresh French Fries"] = "Fries"

# Updating a food item
food_stands["Pronto Pups"] = "Footlong Corn Dogs"

# Removing a food stand
del food_stands["Big Fat Bacon"]
print("\nAfter adding Fries stand, updating Pronto Pups and removing Big Fat Bacon: ")
print(food_stands)

# Using Tuples
attractions = [
    ("Giant Slide", "East of the Grandstand"),
    ("Skyride", "Near Dan Patch Avenue")
]

# Printing the attractions
print("\nFair attractions:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

# Adding a new attraction
new_attraction = ("Haunted House", "Near the Midway")
attractions.append(new_attraction)
print("\nAfter adding a new attraction:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

# Using sets for unique fair activities
activities = {"Riding the Giant Slide", "Watching the Parade"}

print("\nInitial set of activities:")
print(activities)

# Trying to add a duplicate activity
activities.add("Watching the Parade")
print("\nAfter trying to add a duplicate activity:")
print(activities)

# Removing an activity
activities.remove("Riding the Giant Slide")
print("\nAfter removing an activity:")
print(activities)
'''Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

 Correct the bathroom area
areas[-1]=10.50

 Change "living room" to "chill zone"
areas[4]="chill zone"
print(areas)

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = ["pool house",24.5]+ areas
print(areas_1)
# Add garage data to areas_1, new list is areas_2
areas_2 = ["garage",15.45]+areas_1
print(areas_2)

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
print(y)'''
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print (areas)
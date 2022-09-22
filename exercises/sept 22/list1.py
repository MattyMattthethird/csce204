toys = ["lego", "pony", "bike", "trains", "pool"]

#print(toys[2])   # prints bike
#print(toys[4])  # prints pool
toys.append("skipping rope")

# display all of the toys
# loop from 0 to 4 and print the numbers
#for i in range(len(toys)):
#    print(f"{i+1}. {toys[i]}")

# loop through toys 
for item in toys:
    print(item)
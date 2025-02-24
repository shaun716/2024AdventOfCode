# Initializing variables to be used later
total_distance = 0
new_list1 = []
new_list2 = []

#Opening and parsing data from input.txt
fs = open("input.txt")
for i in fs:
    new_list1.append(i[8:-1])
    new_list2.append(i[0:5])

#Sorting lists
new_list1.sort()
new_list2.sort()

#Iterating through num_list1, subtracting value of new_list2 from new_list1 at each iteration to calculate distance
for i in range(len(new_list1)):

    #Result of subtraction is passed to int() and then abs()
    total_distance += abs(int(new_list1[i]) - int(new_list2[i]))

print(f"Total distance = {total_distance}")

fs = open("input.txt")
new_list1 = []
new_list2 = []
total_distance = 0

for i in fs:
    new_list1.append(i[8:-1])
    new_list2.append(i[0:5])

new_list1.sort()
new_list2.sort()

for i in range(len(new_list1)):
    total_distance += abs(int(new_list1[i]) - int(new_list2[i]))
print(f"Total distance = {total_distance}")

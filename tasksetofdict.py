StudentsDetails = [
    {"StudentName": "Kaaveri",
     "StudentId.No": "ST003", 
     "StudentMarks": [100,87,78,65,92]},

    {"StudentName": "Praveen", 
     "StudentId.No": "ST001", 
     "StudentMarks": [50,88,62,75,45]},

    {"StudentName": "Barath", 
     "StudentId.No": "ST002", 
     "StudentMarks": [58,79,100,99,80]}]

# Step 1: Add Total
for i in StudentsDetails:
    total = 0
    for m in i["StudentMarks"]:
        total += m
    i["Total"] = total
print(StudentsDetails,"after total")

# Step 2: Sort by Total (Descending)
for i in range(len(StudentsDetails)):
    for j in range(i+1, len(StudentsDetails)):
        if StudentsDetails[i]["Total"] < StudentsDetails[j]["Total"]:
            StudentsDetails[i], StudentsDetails[j] = StudentsDetails[j], StudentsDetails[i]
print(StudentsDetails,"After sorting")

# Step 3: Assign Rank
rank = 1
for i in StudentsDetails:
    i["Rank"] = rank
    rank += 1
print(StudentsDetails,"After Ranking")




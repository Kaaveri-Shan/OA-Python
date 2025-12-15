StudentsDetails = [
    {"StudentName": "Kaaveri",
     "StudentId.No": "ST003",
     "StudentMarks": [100,87,78,65,92]},

    {"StudentName": "Praveen",
     "StudentId.No": "ST001",
     "StudentMarks": [50,88,62,75,45]},

    {"StudentName": "Barath",
     "StudentId.No": "ST002",
     "StudentMarks": [58,79,100,99,80]},

     {"StudentName": "Sandhiya",
     "StudentId.No": "ST004",
     "StudentMarks": [78,99,100,99,80]},

     {"StudentName": "Nithiya",
     "StudentId.No": "ST005",
     "StudentMarks": [38,49,50,29,10]},

     {"StudentName": "Niveda",
     "StudentId.No": "ST006",
     "StudentMarks": [50,50,50,50,50]}]

# Step 1: Add Total
for i in StudentsDetails:
    total = 0
    for m in i["StudentMarks"]:
        total += m
    i["Total"] = total

# Step 2: Sort by Total (Descending)
for i in range(len(StudentsDetails)):
    for j in range(i+1, len(StudentsDetails)):
        if StudentsDetails[i]["Total"] < StudentsDetails[j]["Total"]:
            StudentsDetails[i], StudentsDetails[j] = StudentsDetails[j], StudentsDetails[i]

# Step 3: Assign Rank
rank = 1
for i in StudentsDetails:
    i["Rank"] = rank
    rank += 1

# Step 4: Assign Grade
for i in StudentsDetails:
    total = i["Total"]

    if 450 <= total <= 500:
        i["Grade"] = "You have scored A+ Grade ___EXCELLENT___"
    elif 400 <= total <= 449:
        i["Grade"] = "You have scored B Grade ___VERY GOOD___"
    elif 300 <= total <= 399:
        i["Grade"] = "You have scored C Grade ___GOOD___"
    elif 240 <= total <= 299:
        i["Grade"] = "You have scored D Grade ___AVERAGE___"
    else:
        i["Grade"] = "Need Improvement ___FAILED___"

# Final Output
for item in StudentsDetails:
    print(item)

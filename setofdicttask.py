# StudentsDetails = [{"StudentName" : "Kaaveri",
#                     "StudentId.No" : "ST003",
#                     "StudentMarks" : [100,87,78,65,92]},

#                     {"StudentName" : "Praveen",
#                     "StudentId.No" : "ST001",
#                     "StudentMarks" : [50,88,62,75,45]},
                    
#                     {"StudentName" : "Barath",
#                     "StudentId.No" : "ST002",
#                     "StudentMarks" : [58,79,100,99,80]}]


# for student in StudentsDetails:
#     student["Total"] = sum(student["StudentMarks"])

# for student in StudentsDetails:
#     print(student)

# current_rank = 1
# for student in StudentsDetails:
#     student["Rank"] = current_rank
#     current_rank += 1
# print(current_rank)

# for student in StudentsDetails:
#     print("Name:", student["StudentName"], 
#           "Total:", student["Total"], 
#           "Rank:", student["Rank"])
# # totals = set()
# # for i in StudentsDetails:
# #     total = sum(i["StudentMarks"])
# #     totals.add(total)
# # totals_list = list(totals)
# # totals_list.sort()       
# # sorted_list = totals_list[::-1]  
# # print(sorted_list)
# for i in range(len(StudentsDetails)):
#     total = 0
#     for mark in StudentsDetails[i]["StudentMarks"]:
#         total += mark
#     StudentsDetails[i] = {"StudentName": StudentsDetails[i]["StudentName"], "Total": total}

# for i in range(len(StudentsDetails)):
#     for j in range(i+1, len(StudentsDetails)):
#         if StudentsDetails[i]["Total"] < StudentsDetails[j]["Total"]:
#             temp = StudentsDetails[i]
#             StudentsDetails[i] = StudentsDetails[j]
#             StudentsDetails[j] = temp

# current_rank = 1
# for student in StudentsDetails:
#     student["Rank"] = current_rank
#     current_rank += 1

# print(StudentsDetails)
StudentsDetails = [
    {"StudentName": "Kaaveri", "StudentMarks": [100,87,78,65,92]},
    {"StudentName": "Praveen", "StudentMarks": [50,88,62,75,45]},
    {"StudentName": "Barath",  "StudentMarks": [58,79,100,99,80]}
]

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

# Step 3: Assign Rank
rank = 1
for i in StudentsDetails:
    i["Rank"] = rank
    rank += 1

print(StudentsDetails)

    
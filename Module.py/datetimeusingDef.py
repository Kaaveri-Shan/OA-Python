import datetime

# Getting todays date
today = datetime.date.today()
print(today)

# # Creating a specific date
# Birthday = datetime.date(2001, 8, 17)
# print(Birthday)

# # Accessing Date's Components
# d1 = datetime.date.today()
# print("Year :", d1.year)
# print("Month:", d1.month)
# print("Date  :", d1.day)

# # Getting Currect Date and Time
# now = datetime.datetime.now()
# print(now)

# # Formatting date using strftime()
# d = datetime.date.today()
# print(d.strftime("%d/%m/%Y "))
# print(d.strftime("%A"))
# print(d.strftime("%B"))

# # strftime() → converts date to readable string
# # %d → date
# # %m → month
# # %Y → year
# # %A → day name
# # %B → month name

# # Adding and subtracting dates (timedelta)
# today = datetime.date.today()
# future = today + datetime.timedelta(days=10)
# past = today - datetime.timedelta(days=5)
# print("Future Date:", future)
# print("Past Date  :", past)

# # Find the difference between dates
# bday = datetime.date(2026, 8, 17)
# TodayDate = datetime.date.today()
# diff = bday - TodayDate
# print("Your Bday comes in ",diff.days,"Days")

# user age count
dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
# dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()

# age = today.year - dob.year
# print("User Age:", age, "years")

def displayData(dob_input):
  dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
  age = today.year - dob.year
  print("User Age:", age, "years")
  days_lived = (today - dob).days
  months_lived = days_lived // 30
  years_lived = days_lived // 365
  print("Age:", age, "years")
  print("Days lived:", days_lived)
  print("Months lived:", months_lived)
  print("Years lived:", years_lived)

displayData(dob_input)


# def diff21(n):
#     if n > 21:
#         return 2 * abs(n - 21)
#     return abs(n
from datetime import date, timedelta
"""
This script will calculate the amount of vacation time you will have accrued by a give date.

Inputs:
    - Desired vacation date
    - Current amount of vacation time you have

** Notes **
    - If your desired vacation date happens to be a pay day, the vacation time will include the time you recieve on that pay day.
        - Ex: If you have zero vacation time at the start of a pay period and you want to take time off the Friday after next (pay day) you will have accrued 7.3 hours by that Friday.
"""

# Prompt user for desired vaction day and create targetDate datetime object, with format error handling
while True:
    try:
        vacationDate = input("When do you want to go on vacation?\nFormat: MM/DD/YYYY \n>> ")
        vacationMonth = vacationDate[:2]
        vacationDay = vacationDate[3:5]
        vacationYear = vacationDate[6:]
        targetDay = date(int(vacationDate[6:]), int(vacationDate[:2]), int(vacationDate[3:5]))

    except ValueError:
        print("Please check the format and try again.\n")
        continue

    else:
        break

# Prompt user for current amount of vacation
vacationTime = float(input("How much vacation time do you currently have? (in hours)\n>> "))

# Get today's date datetime object and create timedelta between now and targetDay
now = date.today()
diff = targetDay - now

# Make list of datetime objects for all days from now until targetDay
days = [now + i * timedelta(days=1) for i in range(0, diff.days + 1)]

# Make list of paydays (this arbitrarily starts on May 11th 2018)
paydayZero = date(2018, 4, 27)
paydays = [paydayZero + i * timedelta(days=14) for i in range(0, int(diff.days))]

# Find how many paydays are in days and calculate the amount of vacation time
paydayCount = 0
for d in range(0, diff.days + 1):
    for pd in range(0, int(diff.days)):
        if days[d] == paydays[pd]:
            paydayCount += 1

vacationTime += paydayCount * 7.3845

# Print vacation balance
print("You will have %.1f days (%.1f hours) of vacation time by %s/%s/%s." % (vacationTime / 8, vacationTime, vacationMonth, vacationDay, vacationYear))

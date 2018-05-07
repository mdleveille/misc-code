from datetime import date, timedelta

# Prompt user for desired vaction day and create targetDate datetime object
while True:
    try:
        vacationDate = input("When do you want to go on vacation?\nFormat: MM/DD/YYYY \n>> ")
        vacationMonth = vacationDate[:2]
        vacationDay = vacationDate[3:5]
        vacationYear = vacationDate[6:]
        targetDay = date(int(vacationDate[6:]), int(vacationDate[:2]), int(vacationDate[3:5]))

    except ValueError:
        print("Please check your format and try again.\n")
        continue

    else:
        break

# Prompt user for current amount of vacation
vacationTime = float(input("How much vacation time do you currently have? (in hours)\n>> "))

# Get today's date datetime object and create timedelta between now and targetDay
now = date.today()
diff = targetDay - now

# Make list of datetime objects for all days from now until targetDay
days = [now + i * timedelta(days=1) for i in range(0, diff.days)]

# Make list of paydays (this arbitrarily starts on May 11th 2018)
paydayZero = date(2018, 4, 27)
paydays = [paydayZero + i * timedelta(days=14) for i in range(0, int(diff.days))]

# Find how many paydays are in days and calculate the amount of vacation time
paydayCount = 0
for d in range(0, diff.days):
    for pd in range(0, int(diff.days)):
        if days[d] == paydays[pd]:
            paydayCount += 1
vacationTime += paydayCount * 7.3845

# Print vacation balances
print("You will have %.1f days of vacation time by %s/%s/%s." % (vacationTime / 8, vacationMonth, vacationDay, vacationYear))

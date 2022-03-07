from ast import If


YearB = 1999
MonthB = 3
dayB = 13

Year = 2022
Month = 2
Day = 23
totalDays = 0

for YearB in range(Year-2):
    if YearB == 2000:
        totalDays += 364
    elif YearB == 2004:
        totalDays +=364
    elif YearB ==2008:
        totalDays +=364
    elif YearB == 2012:
        totalDays +=364
    elif YearB == 2016:
        totalDays += 364
    elif YearB == 2020:
        totalDays += 364
    else:
        totalDays += 365
    
totalDays += 72

totalDays +=54

totalDays = (totalDays%3) + 1 
    
print(f"{totalDays}")


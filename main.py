Weight = open('weight', 'a')
Number_Of_Days = open('number of days', 'w')
weekly_average = open('Weekly Average', 'a')
j = int(input('weight: '))
day = 0
if day > day - 1:
    day += 1
Number_Of_Days.writelines(str(day))
days = f'day {day}'
weight = f'weight {j}'
W = str((days, weight))
Weight.writelines(W)
def WeeklyAverage():
    for i, k in Weight.readline():
        WeeksAverage = sum(k)
        return WeeksAverage
    weekly_average.writelines(str(WeeklyAverage()))

print(WeeklyAverage())
Weight.close()
Number_Of_Days.close()
weekly_average.close()

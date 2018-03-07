print("""
Gregorian Calendar starts from 1582
You can find out day of week of any date from the year 1582 onwards
""")
# subscripts
weekday=("THURSDAY","FRIDAY","SATURDAY","SUNDAY","MONDAY","TUESDAY","WENSDAY")
# month and days in month for a non leap year
monthanddaysn=[0,('January',31),('February',28),('March',31),('April',30),('May',31),('June',30),\
              ('July',31),('August',31),('September',30),('October',31),('November',30),('December',31)]
# month and days in month for a leap year
monthanddaysl= [0, ('January', 31), ('February', 29), ('March', 31), ('April', 30), ('May', 31), ('June', 30), \
                    ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30),
                    ('December', 31)]
monthss=['January','February','March','April','May','June','July','August','September','October','November','December',]
# get the year, month and date from user.
year=input('Enter the Year: ')
if year.isdigit():                                                  # year validation
    year=int(year)
else:
    print('Invalid year, program will exit now')
    exit()
month=input('Enter the Month: ')
if month.isdigit()and 0<int(month)<13:                             #  month validation
    month=int(month)
else:
    print('Invalid month, program will exit now')
    exit()

day=input('Enter the Date: ')
days_in_year=monthanddaysn
if year % 4 == 0:
    days_in_year = monthanddaysl
    if year % 100 == 0:
        days_in_year = monthanddaysn
    if year % 400 == 0:
        days_in_year = monthanddaysl

if day.isdigit() and 0<int(day)<=int(days_in_year[month][1]):          # day validation
    day=int(day)
else:
    print('%d %s has only %s days, program will exit now'%(year,monthss[month],days_in_year[month][1]))
    exit()

"""
A year is considered leap year if:
1. if the year is divisible by 4
2. If the year can be evenly divided by 100, it is NOT a leap year, unless it is divisible by 400.
"""
#find the total number of leap years and non leap years
by4=((year-1580)//4) #-1580 use to remove the no of leap years less than 1582. //4 used to find the years divisible by 4.

if (year-1580)%4 ==0: #if user enter a leap year, we need to exclude the entered leap year from the total year calculation
    by4=by4-1
if year<1584: # no leap years between 1582 and 1584
    by4=0
by100=(year//100)-15 #//100 use to find all years divisible by 100. -15 will remove all years divisible by 100 till 1582
by400=(year//400)-3  #//400 use to find all years divisible by 400. -3 will remove all years divisible by 400 till 1582
noofleapyear=by4-by100+by400
#print(year,month,day)
# get the months and respective dates for leap year /non leap year
monthanddays=monthanddaysn
if year % 4 == 0:
    monthanddays = monthanddaysl
    if year % 100 == 0:
        monthanddays = monthanddaysn
    if year % 400 == 0:
        monthanddays = monthanddaysl
daysinmonth=0
# Find the total numnber of days in the entered year
i=1
while i < month:
    daysinmonth=daysinmonth+monthanddays[i][1]
    i=i+1
#find total number of day from 1-Jan-1582 to the date entered.
totaldays=((year-noofleapyear-1582)*365)+(noofleapyear*366)+daysinmonth+day
weekofday=weekday[totaldays%7]
print(weekofday)

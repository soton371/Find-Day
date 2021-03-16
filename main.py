import math
import datetime

x = datetime.datetime.now()
try:
    day = int(input("enter day(ex.16): "))
    if day>0 and day<32:
        month = int(input("enter month(ex.3): "))
        if month > 0 and month < 13:
            year = int(input("enter year(ex.2021): "))
        else:
            print('please enter valid month')
    else:
        print('please enter valid day')

except:
    print('please enter integer value')
    exit()

if day==x.day and month==x.month and year==x.year:
    print(x.strftime("%A"))
    exit()

if year < 1000:
    print('your year is invalid')
    exit()

if month==4 and day>30 or month==6 and day>30 or month==8 and day>30 or month==9 and day>30 or month==11 and day>30:
    print('please enter valid day!')
    exit()
elif month==2:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                if day>29:
                    print('please enter valid day')
                    exit()
            else:
                if day>28:
                    print('please enter valid day')
                    exit()
        else:
            if day > 29:
                print('please enter valid day')
                exit()
    else:
        if day > 28:
            print('please enter valid day')
            exit()

if month == 1:
    monthS = str(month)
    monthR = monthS.replace(monthS, '11')
    monthI = int(monthR)
elif month == 2:
    monthS = str(month)
    monthR = monthS.replace(monthS, '12')
    monthI = int(monthR)
elif month == 3:
    monthS = str(month)
    monthR = monthS.replace(monthS, '1')
    monthI = int(monthR)
elif month == 4:
    monthS = str(month)
    monthR = monthS.replace(monthS, '2')
    monthI = int(monthR)
elif month == 5:
    monthS = str(month)
    monthR = monthS.replace(monthS, '3')
    monthI = int(monthR)
elif month == 6:
    monthS = str(month)
    monthR = monthS.replace(monthS, '4')
    monthI = int(monthR)
elif month == 7:
    monthS = str(month)
    monthR = monthS.replace(monthS, '5')
    monthI = int(monthR)
elif month == 8:
    monthS = str(month)
    monthR = monthS.replace(monthS, '6')
    monthI = int(monthR)
elif month == 9:
    monthS = str(month)
    monthR = monthS.replace(monthS, '7')
    monthI = int(monthR)
elif month == 10:
    monthS = str(month)
    monthR = monthS.replace(monthS, '8')
    monthI = int(monthR)
elif month == 11:
    monthS = str(month)
    monthR = monthS.replace(monthS, '9')
    monthI = int(monthR)
elif month == 12:
    monthS = str(month)
    monthR = monthS.replace(monthS, '10')
    monthI = int(monthR)

if monthI == 12:
    newYear = year-1
    yearConvert = str(newYear)
    yearLast = yearConvert[2:]
    yearFirst = yearConvert[:2]
else:
    yearConvert = str(year)
    yearLast = yearConvert[2:]
    yearFirst = yearConvert[:2]

yearLastConvert = int(yearLast)
yearFirstConvert = int(yearFirst)

monthF = (13*monthI-1)/5
yearLastConvertFormula = yearLastConvert/4
yearFirstConvertFormula = yearFirstConvert/4


m = math.trunc(monthF)
d = math.trunc(yearLastConvertFormula)
c = math.trunc(yearFirstConvertFormula)


f = day + m + yearLastConvert + d + c - 2*yearFirstConvert


if f<0:
    n = f%7

    if n == 0:
        print('Sunday')
    elif n == 1:
        print('Monday')
    elif n == 2:
        print('Tuesday')
    elif n == 3:
        print('wednesday')
    elif n == 4:
        print('Thursday')
    elif n == 5:
        print('Friday')
    elif n == 6:
        print('Saturday')
else:
    r = f % 7
    if r == 0:
        print('Sunday')
    elif r == 1:
        print('Monday')
    elif r == 2:
        print('Tuesday')
    elif r == 3:
        print('wednesday')
    elif r == 4:
        print('Thursday')
    elif r == 5:
        print('Friday')
    elif r == 6:
        print('Saturday')


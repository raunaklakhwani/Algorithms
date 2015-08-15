days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def getDaysInMonth(month, year):
    if isLeapYear(year):
        if month == 2:
            return 29
        else:
            return days[month]
    else:
        return days[month]

def calculateNumberOfSundays(year):
    s = 0
    day = 0
    for y in xrange(1900, year):
        if day == 6 or (day == 5 and isLeapYear(y)):
            s += 53
            day = 0
        elif isLeapYear(y):
            s += 52
            day = (day + 2) % 7
        else:
            s += 52
            day = (day + 1) % 7
            
    return s
    


def calculateDay(d, month, year):
    day = 0
    for y in xrange(1900, year):
        if isLeapYear(y):
            day = (day + 2) % 7
        else:
            day = (day + 1) % 7
    
    for m in xrange(1, month):
        daysInMonth = getDaysInMonth(m, year)
           
        day = (day + (daysInMonth % 7)) % 7

    day = (day + ((d - 1) % 7)) % 7
        
    return day


def calculateSundays(d1, m1, y1, d2, m2, y2):
    s = 0
    day = calculateDay(d1, m1, y1)
    if day == 0 :
        s = 1
    if y1 != y2:
        daysInMonth = getDaysInMonth(m1, y1)
        day = (day + (daysInMonth - d1 + 1) % 7) % 7
        m1 = m1 + 1
        if m1 >  12:
            m1 = 1
        
    
    
    
       

for year in xrange(1900, 1920):
    print year, day[calculateDay(1, 1, year)]            
print day[calculateDay(12, 12, 1990)]
            
            
            

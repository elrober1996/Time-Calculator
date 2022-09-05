def add_time(start, duration, day = ""):
    clean_baseT = time_clean(start)
    clean_addT = time_clean(duration)
    sumList = timeSum(clean_baseT, clean_addT)
    dateString = dateConv(sumList)
    passed_days = sumList[2]
    result = dateString 
    if not(day == ""):
        result += ", "  + dayGiver(day, passed_days)
    if passed_days == 1:
        result += " (next day)"
    elif passed_days > 1:
        result += " (" + str(passed_days) + " days later)"
    return result  
    

# returns a list[hr24_format_int, min_int]
def time_clean(time_var):
    time = time_var.split()
    hr_min = time[0].split(":")
    #hr_format = time[1]
    hr = int(hr_min[0])
    if len(time) > 1:
        hr_format = time[1]
        if hr_format == "PM":
            hr += 12
    min = hr_min[1]
    if min == "00":
        min = 0
    else:
        min = int(min.lstrip("0"))
    return [hr, min]


# sums the too dates
# return num of dates passed (if any after the sum) and the new date
# 12 AM is represented with 0 in the return
def timeSum(baseT, addT):
    passed_days = 0
    hr_sum = baseT[0] + addT[0]
    min_sum = baseT[1] + addT[1]
    # minutes clean up if they make an hour or more, and added the new hour(s)
    if min_sum >= 60:
        leftover_min = min_sum % 60
        newhrs = min_sum // 60
        hr_sum += newhrs
        min_sum = leftover_min
    if hr_sum == 24:
        passed_days = 1
    elif hr_sum > 24:
        passed_days += hr_sum // 24
        hr_sum = hr_sum % 24
    return [hr_sum, min_sum, passed_days]

def dateConv(the_date):
    strdate = ""
    if the_date[0] == 0 or the_date[0] == 24 :
        strdate += "12:" + str(the_date[1]).zfill(2) + " AM"
        return strdate
    elif the_date[0] == 12:
        strdate += "12:" + str(the_date[1]).zfill(2) + " PM"
        return strdate
    elif the_date[0] > 12:
        strdate += str(the_date[0] - 12) + ":" + str(the_date[1]).zfill(2) + " PM"
        return strdate
    else:
        strdate += str(the_date[0]) + ":" + str(the_date[1]).zfill(2) + " AM"
        return strdate
    
def dayGiver(day, passed_days):
    days = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
    cleanedDay =  day.title()
    dayIndex = 0
    if cleanedDay == days[0]:
        dayIndex = 0
    elif cleanedDay == days[1]:
        dayIndex = 1
    elif cleanedDay == days[2]:
        dayIndex = 2
    elif cleanedDay == days[3]:
        dayIndex = 3
    elif cleanedDay == days[4]:
        dayIndex = 4
    elif cleanedDay == days[5]:
        dayIndex = 5
    elif cleanedDay == days[6]:
        dayIndex = 6
    newIndex = dayIndex + passed_days
    if newIndex > 6:
        return days[newIndex % 7]
    return days[newIndex]
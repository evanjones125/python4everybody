def add_time(start, duration, day = None): 
    # create output string to be concatenated
    output = ''

    # keep track of days that have elapsed
    days_later = 0

    # create list with days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # store input hours and minutes in variables in 24hr format
    start_hour = int(start[:start.find(':')])
    start_min = int(start[start.find(':') + 1:start.find(':') + 3])
    dur_hour = int(duration[:duration.find(':')])
    dur_min = int(duration[duration.find(':') + 1:duration.find(':') + 3])
    if start[-2] is 'P': start_hour += 12

    # create output variables to store sums of start and duration values
    output_hour = start_hour + dur_hour
    output_min = start_min + dur_min

    # if output_hour exceeds 24, increment days_later and subtract 24 from output_hour
    while output_hour > 22:
        output_hour -= 24
        days_later += 1

    # increment output_hour if output_min > 60 and add a 0 to output_min if < 10
    if output_min > 60:
        output_hour += 1
        output_min -= 60

    if output_min < 10:
        output_min = '0' + str(output_min)

    # concatenate output with time and AM/PM
    if output_hour < 12 and output_hour > 0:
        output += str(output_hour) + ':' + str(output_min) + ' AM'

    if output_hour > 12:
        output_hour -= 12
        output += str(output_hour) + ':' + str(output_min) + ' PM'

    if output_hour == 12:
        output += '12:' + str(output_min) + ' PM'
    
    if output_hour == 0:
        output += '12:' + str(output_min) + ' AM'

    # concatenate output with day of week (if applicable)
    if day:
        
        # link third argument to index in days list
        days_index = 0
        for idx, i in enumerate(days):
            if i.lower() == day.lower():
                days_index = idx
                # print(days_index)

        # find the day of the week after adding time
        output += ', ' + days[(days_index + days_later) % 7]
        
    # concatenate output with days_later value (if applicable)
    if days_later is 1: output += ' (next day)'
    if days_later > 1: output += ' (' + str(days_later) + ' days later)'

    return output
    return [output_hour, output_min, days_later]
    return [start_hour, start_min, dur_hour, dur_min]

print(add_time('3:00 PM', '3:10')) # '6:10 PM'
print(add_time('11:30 AM', '2:32', 'Monday')) # '2:02 PM, Monday'
print(add_time('11:43 AM', '00:20')) # '12:03 PM'
print(add_time('10:10 PM', '3:30')) # '1:40 AM (next day)'
print(add_time('11:43 PM', '24:20', 'tueSday')) # '12:03 AM, Thursday (2 days later)'
print(add_time('6:30 PM', '205:12')) # '7:42 AM (9 days later)'
print(add_time('8:16 PM', '466:02', 'tuesday')) # '6:18 AM, Monday (20 days later)'
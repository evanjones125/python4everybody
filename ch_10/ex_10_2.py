def hours(file):
    handle = open(file)
    hours = []
    store = {}

    # take the two digits prior to the first instance of ':' and store in a list
    for line in handle:
        if line.startswith("From "):
            hour = line[line.find(':') - 2] + line[line.find(':') - 1]
            hours.append(hour)

    # populate store dictionary with hours values and their frequencies
    for hour in hours:
        if hour in store:
            store[hour] += 1
        else:
            store[hour] = 1

    # sort store and print each property as a tuple
    for i in sorted(store):
        print(i, store[i])

print(hours('mbox-short.txt'))
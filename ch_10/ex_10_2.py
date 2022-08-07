def hours(file):
    handle = open(file)
    hours = []
    store = {}

    # if line starts with from, take the two digits prior to the first instance of ':'
    for line in handle:
        if line.startswith("From "):
            hour = line[line.find(':') - 2] + line[line.find(':') - 1]
            hours.append(hour)

    for hour in hours:
        if hour in store:
            store[hour] += 1
        else:
            store[hour] = 1

    for i in sorted(store):
        print(i, store[i])

print(hours('mbox-short.txt'))
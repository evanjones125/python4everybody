def senders(file):
    fh = open(file)
    count = 0

    for line in fh:
        if line.startswith('From '):
            new_list = line.split()
            print(new_list[1])
            count += 1

    return "there were {count} lines in the file with From as the first word".format(count = count)

print(senders('mbox-short.txt'))
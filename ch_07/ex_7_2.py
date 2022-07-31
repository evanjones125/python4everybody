# Use the file name mbox-short.txt as the file name
def confidence(file):
    fh = open(file)
    total = 0
    counter = 0

    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            total += float(line[line.find('0'):])
            counter += 1
        if not line.startswith("X-DSPAM-Confidence:"):
            continue    
    return "Average spam confidence:", (total / counter)

print(confidence('mbox-short.txt'))
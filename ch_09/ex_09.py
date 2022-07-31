name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# extract all emails and store in a list
store = []
for line in handle:
    if line.startswith('From '):
        new_list = line.split()
        store.append(new_list[1])

# create a histogram of the frequencies of each email address
hist = {}    
for email in store:
    hist[email] = hist.get(email, 0) + 1

# find which key of the hist object has the highest value
count = 0
output = ''
for i in hist:
    if hist[i] > count:
        count = hist[i]
        output = i

print(output, count)
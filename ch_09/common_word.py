def common_word(file):
    # get text from file
    handle = open(file)
    store = []
    for line in handle:
        store.append(line.split())
    flattened_store = [element for sublist in store for element in sublist]
    string = " ".join(flattened_store)

    # remove punctuation from text
    punc = ''',.'"!'''
    for letter in string:
        if letter in punc:
            string = string.replace(letter, "")

    # create histogram of the frequencies of each word
    fixed = string.lower().split()
    hist = {}
    for word in fixed:
        hist[word] = hist.get(word, 0) + 1

    # find which key of hist has the highest value
    count = 0
    highest = ''
    for key in hist:
        if hist[key] > count:
            count = hist[key]
            highest = key

    return "the word that appears most often is {highest}; it appears {count} times".format(highest = highest, count = count)

print(common_word('alien_superstar.txt'))
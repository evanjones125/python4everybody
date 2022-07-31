def common(file):
    handle = open(file)
    store = {}
    for line in handle:
        line = line.rstrip()
        words = line.split()
        for word in words:
            store[word] = store.get(word, 0) + 1
    return store

print(common('lorem.txt'))
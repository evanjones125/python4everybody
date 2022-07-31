# def common_word(file):
#     handle = open(file)
#     store = []
#     for line in handle:
#         # words = line.split()
#         new_list = line.split()
#         store.append(new_list[1])
#     return store

# print(common_word('lorem.txt'))


handle = open('lorem.txt')

# extract all emails and store in a lis
# store = []
for line in handle:
    line = line.rstrip()
    print(line)

# print(store)
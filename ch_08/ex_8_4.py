def new(file):
    fh = open(file)
    lst = []
    for line in fh:
        lst.append(line.split())
    
        
    flat_list = []
    for xs in lst:
        for x in xs:
            flat_list.append(x)
        
    flat_list.sort()

    output = []

    for i in flat_list:
        if i not in output:
            output.append(i)

    return output

print(new('romeo.txt'))